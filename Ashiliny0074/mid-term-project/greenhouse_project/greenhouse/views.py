from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import GreenhouseMetric, UserSetting
from .serializers import GreenhouseMetricSerializer, UserSettingSerializer

class GreenhouseMetricViewSet(viewsets.ModelViewSet):
    serializer_class = GreenhouseMetricSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GreenhouseMetric.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserSettingViewSet(viewsets.ModelViewSet):
    serializer_class = UserSettingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserSetting.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from django_filters.rest_framework import DjangoFilterBackend

class GreenhouseMetricViewSet(viewsets.ModelViewSet):
    serializer_class = GreenhouseMetricSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['temperature', 'humidity', 'soil_moisture', 'light_level', 'created_at']

    def get_queryset(self):
        return GreenhouseMetric.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

