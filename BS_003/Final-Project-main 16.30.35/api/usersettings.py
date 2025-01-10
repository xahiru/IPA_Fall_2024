from django.db import models
from django.contrib.auth.models import User

class Metric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    light_level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Metric for {self.user.username} at {self.timestamp}"

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    temperature_threshold = models.FloatField()
    humidity_threshold = models.FloatField()
    soil_moisture_threshold = models.FloatField()
    light_level_threshold = models.FloatField()

    def __str__(self):
        return f"Settings for {self.user.username}"
