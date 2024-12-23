from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GreenHouseMetricViewSet

router = DefaultRouter()
router.register(r'metrics', GreenHouseMetricViewSet)

urlpatterns = [
    path('', include(router.urls)),
]