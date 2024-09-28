from django.db import models
from accounts.models import User

class ArtisanProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    skills = models.ManyToManyField('Skill', blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)  
    total_reviews = models.IntegerField(default=0)  

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    

class Skill(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    name = models.CharField(max_length=100)

class Service(models.Model):
    artisan_profile = models.ForeignKey(ArtisanProfile, related_name='services', on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.service_name