from django.contrib.auth.models import User
from rest_framework import serializers
from .models import GreenhouseData, UserControl


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class GreenhouseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenhouseData
        fields = ['id', 'temperature', 'humidity', 'soil_moisture', 'light_level', 'timestamp']

class UserControlSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserControl
        fields = ['id', 'user', 'temp_threshold', 'humidity_threshold', 'soil_moisture_threshold', 'alert_light_level']