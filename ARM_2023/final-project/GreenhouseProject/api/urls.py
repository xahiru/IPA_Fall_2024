from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GreenhouseMetricViewSet, UserSettingViewSet, UserRegistrationView, UserLoginView, UserLogoutView

router = DefaultRouter()
router.register('metrics', GreenhouseMetricViewSet)
router.register('settings', UserSettingViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', include(router.urls)),  # Includes CRUD views
]