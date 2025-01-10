from django.db import models
from django.contrib.auth.models import User

class Metrics(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    light_level = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
      return f"Metrics recorded at {self.created_at}"

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alert_threshold_temperature = models.FloatField()
    alert_threshold_humidity = models.FloatField()
    alert_threshold_soil_moisture = models.FloatField()
    alert_threshold_light_level = models.FloatField()

def __str__(self):
     return f"Settings for {self.user.user}"
      
