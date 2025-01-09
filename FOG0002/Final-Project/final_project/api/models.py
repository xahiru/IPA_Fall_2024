from django.db import models

class GreenhouseMetrics(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    light_level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Metrics at {self.timestamp}"

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    temp_threshold = models.FloatField(null=True, blank=True)
    humidity_threshold = models.FloatField(null=True, blank=True)
    soil_moisture_threshold = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Settings for {self.user.username}"
