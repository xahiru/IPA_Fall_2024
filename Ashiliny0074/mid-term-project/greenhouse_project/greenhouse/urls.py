from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import GreenhouseMetricViewSet, UserSettingViewSet

router = SimpleRouter()
router.register('metrics', GreenhouseMetricViewSet, basename='metrics')
router.register('settings', UserSettingViewSet, basename='settings')

urlpatterns = [
    path('', include(router.urls)),
]
 
