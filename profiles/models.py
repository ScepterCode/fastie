from django.db import models
from accounts.models import User

class ArtisanProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField('Skill')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    name = models.CharField(max_length=100)
