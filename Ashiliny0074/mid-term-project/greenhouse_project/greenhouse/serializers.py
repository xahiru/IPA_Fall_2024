from rest_framework import serializers
from .models import GreenhouseMetric, UserSetting

class GreenhouseMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenhouseMetric
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = '__all__'
        read_only_fields = ['user']
 
