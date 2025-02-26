from rest_framework import serializers
from .models import GreenHouseMetric

class GreenHouseMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenHouseMetric
        fields = ['id', 'temperature', 'humidity', 'soil_moisture', 'light_level', 'timestamp']
