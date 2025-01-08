from django.contrib import admin
from .models import GreenHouseMetric

class GreenHouseMetricAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'soil_moisture', 'light_level', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('temperature', 'humidity')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

admin.site.register(GreenHouseMetric, GreenHouseMetricAdmin)