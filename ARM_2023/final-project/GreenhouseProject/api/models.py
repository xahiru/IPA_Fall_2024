from django.db import models
from django.contrib.auth.models import User

class GreenhouseMetric(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    light_intensity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f" {self.user.username} - {self.timestamp}"

class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=50, default='light')
    notifications_enabled = models.BooleanField(default=True)
    threshold_temperature = models.FloatField()
    threshold_humidity = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - Settings"

