from django.contrib import admin
from .models import Metrics, UserSettings

class MetricsAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'soil_moisture', 'light_level', 'created_at') 
    search_fields = ('temperature', 'humidity')  
    list_filter = ('created_at',)  
    ordering = ('-created_at',)  


class UserSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'alert_threshold_temperature',
        'alert_threshold_humidity',
        'alert_threshold_soil_moisture',
        'alert_threshold_light_level'
        )  
    search_fields = ('user__username',)  
    list_filter = ('alert_threshold_temperature', 'alert_threshold_humidity')  


admin.site.register(Metrics, MetricsAdmin)
admin.site.register(UserSettings, UserSettingsAdmin)

