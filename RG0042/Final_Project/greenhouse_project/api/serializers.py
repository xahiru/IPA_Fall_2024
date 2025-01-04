from rest_framework import serializers # type: ignore
from .models import Metric, UserSetting

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = '__all__'
        read_only_fields = ['user']  # Ensure the user is set in the view
