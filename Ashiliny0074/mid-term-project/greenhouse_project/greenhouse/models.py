from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class GreenhouseMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    light_level = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Metrics for {self.user.username} at {self.created_at}"

class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alert_temperature = models.FloatField(default=30.0)
    alert_humidity = models.FloatField(default=50.0)
    alert_soil_moisture = models.FloatField(default=30.0)
    alert_light_level = models.FloatField(default=100.0)

    def __str__(self):
        return f"Settings for {self.user.username}"
