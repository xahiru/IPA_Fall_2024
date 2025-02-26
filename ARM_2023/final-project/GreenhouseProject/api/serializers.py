from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GreenhouseMetric, UserSetting
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class GreenhouseMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenhouseMetric
        fields = ['id', 'temperature', 'humidity', 'light_intensity', 'date', 'user']

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = ['user', 'threshold_temperature', 'threshold_humidity']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user