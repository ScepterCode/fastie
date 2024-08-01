from rest_framework import serializers
from .models import ArtisanProfile, ClientProfile, Skill, Location

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

class ArtisanProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    location = LocationSerializer()

    class Meta:
        model = ArtisanProfile
        fields = ['id', 'user', 'bio', 'skills', 'location', 'is_available']

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ['id', 'user', 'company_name']