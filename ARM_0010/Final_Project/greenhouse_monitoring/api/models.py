# from django.db import models
# from django.contrib.auth.models import User

# class GreenhouseMetric(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='metrics')
#     temperature = models.FloatField()
#     humidity = models.FloatField()
#     soil_moisture = models.FloatField()
#     light_level = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Metrics for {self.user.username} at {self.timestamp}"

# class UserSetting(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
#     temperature_threshold = models.FloatField()
#     humidity_threshold = models.FloatField()
#     soil_moisture_threshold = models.FloatField()
#     light_level_threshold = models.FloatField()

#     def __str__(self):
#         return f"Settings for {self.user.username}"


from django.db import models
from django.contrib.auth.models import User

#=========================
class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#=========================


class GreenhouseMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='metrics')
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    light_level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Metrics for {self.user.username} at {self.timestamp}"

class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    temperature_threshold = models.FloatField()
    humidity_threshold = models.FloatField()
    soil_moisture_threshold = models.FloatField()
    light_level_threshold = models.FloatField()

    def __str__(self):
        return f"Settings for {self.user.username}"
