from django.db import models
from django.contrib.auth.models import User

class GreenhouseMetric(models.Model):
    METRIC_TYPES = [
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('soil_moisture', 'Soil Moisture'),
        ('light_level', 'Light Level'),
    ]
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPES)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UserThreshold(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    temperature_threshold = models.FloatField(default=0.0)
    humidity_threshold = models.FloatField(default=0.0)
    soil_moisture_threshold = models.FloatField(default=0.0)
    light_level_threshold = models.FloatField(default=0.0)