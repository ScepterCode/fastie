from rest_framework import serializers
from .models import Service, Booking, Notification

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'client', 'artisan', 'service', 'booking_date', 'status', 'job_id', 'created_at', 'updated_at']
        read_only_fields = ['job_id', 'created_at', 'updated_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'booking', 'message', 'is_read', 'created_at']
        read_only_fields = ['created_at']