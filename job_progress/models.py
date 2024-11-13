
from django.db import models
from django.core.exceptions import ValidationError
from booking.models import Booking

class JobProgress(models.Model):
    STAGE_CHOICES = [
        ('initiation', 'Initiation'),
        ('execution', 'Execution'),
        ('completion', 'Completion')
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('artisan_updated', 'Artisan Updated'),
        ('client_declined', 'Client Declined'),
        ('client_confirmed', 'Client Confirmed')
    ]
    
    booking = models.ForeignKey('booking.Booking', on_delete=models.CASCADE, related_name='job_progress')
    current_stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='initiation')
    initiation_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    execution_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    completion_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job Progress for Booking {self.booking.id}"

    def get_stage_status(self, stage):
        return getattr(self, f'{stage}_status')

    def set_stage_status(self, stage, status):
        setattr(self, f'{stage}_status', status)
        self.save()
