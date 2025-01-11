from django.contrib import admin
from .models import GreenhouseMetric, UserThreshold

admin.site.register(GreenhouseMetric)
admin.site.register(UserThreshold)