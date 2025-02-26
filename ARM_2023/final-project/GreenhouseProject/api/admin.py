from django.contrib import admin
from .models import GreenhouseMetric, UserSetting

class GreenhouseMetricAdmin(admin.ModelAdmin):
    list_display = ('user', 'temperature', 'humidity', 'light_intensity', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'temperature', 'humidity', 'light_intensity')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

admin.site.register(GreenhouseMetric, GreenhouseMetricAdmin)

class UserSettingAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'notifications_enabled', 'threshold_temperature', 'threshold_humidity')
    list_filter = ('user', 'theme')
    search_fields = ('user__username',)

admin.site.register(UserSetting, UserSettingAdmin)