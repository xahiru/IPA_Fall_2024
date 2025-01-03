from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from bolor.views import MetricViewSet 

router = SimpleRouter()
router.register('metrics', MetricViewSet, basename='metric')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
]
