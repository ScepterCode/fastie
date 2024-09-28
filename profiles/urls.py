from django.urls import path
from .views import ArtisanProfileView, ClientProfileView, SearchArtisansView, ToggleAvailabilityView, ArtisanDetailView

urlpatterns = [
    path('artisan/', ArtisanProfileView.as_view(), name='artisan-profile'),
    path('client/', ClientProfileView.as_view(), name='client-profile'),
    path('search/', SearchArtisansView.as_view(), name='search-artisans'),
    path('toggle-availability/', ToggleAvailabilityView.as_view(), name='toggle-availability'),
    path('artisans/search/', SearchArtisansView.as_view(), name='search-artisans'),
    path('artisans/<int:artisan_id>/', ArtisanDetailView.as_view(), name='artisan-detail'),
]
