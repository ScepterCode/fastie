from django.urls import path
from .views import ArtisanProfileView, ClientProfileView, SearchArtisansView, ToggleAvailabilityView

urlpatterns = [
    path('artisan/', ArtisanProfileView.as_view(), name='artisan-profile'),
    path('client/', ClientProfileView.as_view(), name='client-profile'),
    path('search/', SearchArtisansView.as_view(), name='search-artisans'),
    path('toggle-availability/', ToggleAvailabilityView.as_view(), name='toggle-availability'),
]

from django.urls import path
from .views import ArtisanProfileView, ClientProfileView, SearchArtisansView, ToggleAvailabilityView

