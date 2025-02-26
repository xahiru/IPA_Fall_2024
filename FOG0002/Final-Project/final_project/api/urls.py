from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, LoginView, LogoutView, GreenhouseMetricsViewSet, UserSettingsViewSet
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()
router.register(r'metrics', GreenhouseMetricsViewSet, basename='greenhouse-metrics')
router.register(r'settings', UserSettingsViewSet, basename='user-settings')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('api/', include(router.urls)),
]
