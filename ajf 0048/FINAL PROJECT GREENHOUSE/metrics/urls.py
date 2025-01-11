from django.urls import path
from .views import RegisterView, dashboard, GreenHouseMetricViewSet 

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), 
    path('dashboard/', dashboard, name='dashboard'), 
    path('api/metrics/', GreenHouseMetricViewSet.as_view({'get': 'list'}), name='metrics-list'), 

]