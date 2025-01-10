from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Metric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    light_level = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    temperature_threshold = models.FloatField(default=25.0)
    humidity_threshold = models.FloatField(default=60.0)