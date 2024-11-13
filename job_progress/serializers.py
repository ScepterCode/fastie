from rest_framework import serializers
from .models import JobProgress

class JobProgressSerializer(serializers.ModelSerializer):
    booking_id = serializers.IntegerField(read_only=True, source='booking.id')
    
    class Meta:
        model = JobProgress
        fields = ['id', 'booking_id', 'current_stage', 'initiation_status', 
                 'execution_status', 'completion_status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']