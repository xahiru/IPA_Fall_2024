from rest_framework import serializers
from .models import GreenhouseMetric, UserThreshold

class GreenhouseMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenhouseMetric
        fields = '__all__'

class UserThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserThreshold
        fields = '__all__'