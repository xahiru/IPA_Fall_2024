from rest_framework.viewsets import ModelViewSet
from .models import Metric
from .serializers import MetricSerializer
from rest_framework.permissions import IsAuthenticated

class MetricViewSet(ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
