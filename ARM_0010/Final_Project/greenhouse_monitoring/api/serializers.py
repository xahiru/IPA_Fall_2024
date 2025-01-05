from rest_framework import serializers
from .models import GreenhouseMetric, User, UserSetting

class GreenhouseMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenhouseMetric
        fields = '__all__'
        read_only_fields = ('user', 'timestamp')

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = '__all__'
        read_only_fields = ('user',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
