from django.contrib import admin
from .models import Metric, UserSetting

admin.site.register(Metric)
admin.site.register(UserSetting)