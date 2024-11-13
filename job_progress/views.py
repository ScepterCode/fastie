from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import JobProgress
from .serializers import JobProgressSerializer


class JobProgressViewSet(viewsets.ModelViewSet):
    serializer_class = JobProgressSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'artisan_profile'):
            return JobProgress.objects.filter(booking__artisan=user)
        return JobProgress.objects.filter(booking__client=user)

    @action(detail=True, methods=['post'])
    def update_stage(self, request, pk=None):
        """
        Allows artisan to update the current stage of a job progress
        """
        job_progress = self.get_object()
        booking = job_progress.booking

        # Verify the user is the artisan for this booking
        if request.user != booking.artisan:
            return Response(
                {'error': 'Only the assigned artisan can update job progress'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Get the requested stage
        stage = request.data.get('stage')
        if not stage or stage not in dict(JobProgress.STAGE_CHOICES):
            return Response(
                {'error': 'Invalid stage provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validate stage progression
        stages = ['initiation', 'execution', 'completion']
        current_index = stages.index(job_progress.current_stage)
        requested_index = stages.index(stage)

        # Can't skip stages or go backwards
        if requested_index > current_index + 1:
            return Response(
                {'error': 'Cannot skip stages'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if requested_index < current_index:
            return Response(
                {'error': 'Cannot go back to previous stages'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if previous stage is confirmed (except for first stage)
        if requested_index > 0:
            previous_stage = stages[requested_index - 1]
            previous_status = job_progress.get_stage_status(previous_stage)
            if previous_status != 'client_confirmed':
                return Response(
                    {'error': 'Previous stage must be confirmed before proceeding'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Update the stage status
        job_progress.current_stage = stage
        job_progress.set_stage_status(stage, 'artisan_updated')

        # Create notification for client
        notification_data = {
            'recipient': booking.client,
            'booking': booking,
            'notification_type': 'job_progress_update',
            'title': 'Job Progress Update',
            'message': f'Artisan has updated the job progress to {stage} stage. Please confirm or decline.',
            'metadata': {
                'job_progress_id': job_progress.id,
                'stage': stage
            }
        }
        
        # Assuming your notification system has a create_notification function
        from notifications.services import create_notification  # Import your notification service
        create_notification(**notification_data)

        serializer = self.get_serializer(job_progress)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def client_response(self, request, pk=None):
        """
        Allows client to confirm or decline a stage update
        """
        job_progress = self.get_object()
        booking = job_progress.booking

        # Verify the user is the client for this booking
        if request.user != booking.client:
            return Response(
                {'error': 'Only the client can confirm or decline progress'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Get the stage and response
        stage = job_progress.current_stage
        response = request.data.get('response')
        
        if response not in ['confirm', 'decline']:
            return Response(
                {'error': 'Invalid response. Must be either confirm or decline'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the stage is pending client response
        current_status = job_progress.get_stage_status(stage)
        if current_status != 'artisan_updated':
            return Response(
                {'error': 'This stage is not pending client response'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update the stage status based on client response
        new_status = 'client_confirmed' if response == 'confirm' else 'client_declined'
        job_progress.set_stage_status(stage, new_status)

        # Create notification for artisan
        notification_data = {
            'recipient': booking.artisan,
            'booking': booking,
            'notification_type': 'job_progress_response',
            'title': 'Job Progress Response',
            'message': f'Client has {response}ed the {stage} stage.',
            'metadata': {
                'job_progress_id': job_progress.id,
                'stage': stage,
                'response': response
            }
        }
        
        # Using your notification system
        from notifications.services import create_notification
        create_notification(**notification_data)

        serializer = self.get_serializer(job_progress)
        return Response(serializer.data)

