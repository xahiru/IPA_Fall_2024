"""
URL configuration for fianlproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path
from .views import RegisterUserAPIView, LogoutUserAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutUserAPIView.as_view(), name='logout'),
]
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]
from rest_framework.routers import SimpleRouter
from .views import GreenhouseMetricViewSet, UserThresholdViewSet

router = SimpleRouter()
router.register('metrics', GreenhouseMetricViewSet)
router.register('thresholds', UserThresholdViewSet)

urlpatterns += router.urls
from django_filters.rest_framework import DjangoFilterBackend

class GreenhouseMetricViewSet(ModelViewSet):
    ...
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['metric_type', 'timestamp']