from rest_framework import viewsets
from .models import GreenHouseMetric
from .serializers import GreenHouseMetricSerializer

class GreenHouseMetricViewSet(viewsets.ModelViewSet):
    queryset = GreenHouseMetric.objects.all()
    serializer_class = GreenHouseMetricSerializer