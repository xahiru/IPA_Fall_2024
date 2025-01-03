from django.contrib import admin
from .models import Metric, UserSettings

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'soil_moisture', 'light_level', 'timestamp')

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'temp_threshold', 'humidity_threshold')
