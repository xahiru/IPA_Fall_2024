from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import GreenhouseMetric, UserSetting

admin.site.register(GreenhouseMetric)
admin.site.register(UserSetting)
