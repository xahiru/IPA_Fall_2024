from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import GreenhouseMetricViewSet, UserSettingViewSet

router = SimpleRouter()
router.register('metrics', GreenhouseMetricViewSet, basename='metric')
router.register('settings', UserSettingViewSet, basename='setting')

urlpatterns = [
    path('', include(router.urls)),
    
]
