

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import MetricViewSet, UserSettingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'metrics', MetricViewSet)
router.register(r'user-settings', UserSettingViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Authentication URL
] + router.urls  # Combine with the router URLs