from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'job-progress', views.JobProgressViewSet, basename='job-progress')
# router.register(r'job-history', views.JobHistoryViewSet, basename='job-history')
# router.register(r'job-notifications', views.JobNotificationViewSet, basename='job-notifications')

urlpatterns = [
    path('', include(router.urls)),
]