from django.shortcuts import render
from rest_framework import viewsets
from .models import Metrics, UserSettings
from .serializers import MetricsSerializer, UserSettingsSerializer

class MetricsViewSet(viewsets.ModelViewSet):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
# Create your views here.
