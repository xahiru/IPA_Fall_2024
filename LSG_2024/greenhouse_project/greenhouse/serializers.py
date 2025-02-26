from rest_framework import serializers
from .models import Metrics, UserSettings

class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = '__all__'

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = '__all__'