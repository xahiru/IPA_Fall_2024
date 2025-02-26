from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MetricsViewSet, UserSettingsViewSet

# Create a router for automatic URL routing
router = DefaultRouter()
router.register('metrics', MetricsViewSet)
router.register('user-settings', UserSettingsViewSet)

# Define app-specific URLs
urlpatterns = [
    path('', include(router.urls)),
]