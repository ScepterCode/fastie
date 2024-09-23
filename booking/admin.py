from django.contrib import admin
from .models import Service, Booking, Notification

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'client', 'artisan', 'service', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('job_id', 'client__username', 'artisan__username')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'booking', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('recipient__username', 'booking__job_id')

