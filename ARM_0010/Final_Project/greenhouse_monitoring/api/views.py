from requests import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import GreenhouseMetric, UserSetting
from .serializers import GreenhouseMetricSerializer, UserSettingSerializer

class GreenhouseMetricViewSet(ModelViewSet):
    queryset = GreenhouseMetric.objects.all()
    serializer_class = GreenhouseMetricSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserSettingViewSet(ModelViewSet):
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

class GreenhouseMetricViewSet(ModelViewSet):
    queryset = GreenhouseMetric.objects.all()
    serializer_class = GreenhouseMetricSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['timestamp']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





# lllll

@api_view(['GET'])
def get_user(request):
    return Response({'name: "admin"'})

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from .models import GreenhouseMetric
from .serializers import GreenhouseMetricSerializer

class GreenhouseMetricViewSet(viewsets.ModelViewSet):
    queryset = GreenhouseMetric.objects.all()
    serializer_class = GreenhouseMetricSerializer
    authentication_classes = [TokenAuthentication]  # Ensure token authentication is used
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

