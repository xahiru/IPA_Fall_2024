"""
URL configuration for greenhouse project.

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
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from metrics.views import GreenHouseMetricViewSet, dashboard, register
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

# Schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Greenhouse API",
        default_version='v1',
        description="API for monitoring greenhouse conditions",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register(r'metrics', GreenHouseMetricViewSet, basename='metrics')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='metrics/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='metrics/logout.html'), name='logout'),
]