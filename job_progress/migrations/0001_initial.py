# Generated by Django 5.0.7 on 2024-11-13 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_stage', models.CharField(choices=[('initiation', 'Initiation'), ('execution', 'Execution'), ('completion', 'Completion')], default='initiation', max_length=20)),
                ('initiation_status', models.CharField(choices=[('pending', 'Pending'), ('artisan_updated', 'Artisan Updated'), ('client_declined', 'Client Declined'), ('client_confirmed', 'Client Confirmed')], default='pending', max_length=20)),
                ('execution_status', models.CharField(choices=[('pending', 'Pending'), ('artisan_updated', 'Artisan Updated'), ('client_declined', 'Client Declined'), ('client_confirmed', 'Client Confirmed')], default='pending', max_length=20)),
                ('completion_status', models.CharField(choices=[('pending', 'Pending'), ('artisan_updated', 'Artisan Updated'), ('client_declined', 'Client Declined'), ('client_confirmed', 'Client Confirmed')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_progress', to='booking.booking')),
            ],
        ),
    ]
