from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import ArtisanProfile, ClientProfile
from .serializers import ArtisanProfileSerializer, ClientProfileSerializer, ArtisanDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArtisanProfile, Skill, Location 
from rest_framework.permissions import IsAuthenticated

class ArtisanProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ArtisanProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return ArtisanProfile.objects.get(user=self.request.user)

class ClientProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return ClientProfile.objects.get(user=self.request.user)
    
           
           
#Search API (below is the search api)

class SearchArtisansView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        skills = request.GET.getlist('skills')
        location = request.GET.get('location')

        queryset = ArtisanProfile.objects.filter(is_available=True)

        if skills:
            queryset = queryset.filter(skills__name__in=skills)
        if location:
            queryset = queryset.filter(location__name=location)

        serializer = ArtisanProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    

#Availability API 

class ToggleAvailabilityView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        artisan_profile = ArtisanProfile.objects.get(user=request.user)
        artisan_profile.is_available = not artisan_profile.is_available
        artisan_profile.save()
        return Response({'is_available': artisan_profile.is_available})


class ArtisanDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, artisan_id):
        try:
            artisan = ArtisanProfile.objects.get(id=artisan_id)
            serializer = ArtisanDetailSerializer(artisan)
            return Response(serializer.data)
        except ArtisanProfile.DoesNotExist:
            return Response({"error": "Artisan not found"}, status=status.HTTP_404_NOT_FOUND)
