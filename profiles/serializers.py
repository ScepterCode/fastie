from rest_framework import serializers
from .models import ArtisanProfile, ClientProfile, Skill, Location, Service

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

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'price', 'description']

class ArtisanDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    location = serializers.CharField(source='location.name')
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ArtisanProfile
        fields = ['id', 'user', 'bio', 'skills', 'location', 'is_available', 'services']

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'email': obj.user.email,
            'phone_number': obj.user.phone_number  # Assuming you have this field in your User model
        }