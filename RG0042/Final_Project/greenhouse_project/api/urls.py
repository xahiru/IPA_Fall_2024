from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .views import MetricViewSet, UserSettingViewSet

router = DefaultRouter()
router.register(r'metrics', MetricViewSet, basename='metric')
router.register(r'settings', UserSettingViewSet, basename='setting')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('', include(router.urls)),
]
