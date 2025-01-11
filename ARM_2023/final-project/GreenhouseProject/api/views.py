from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import GreenhouseMetric, UserSetting
from .serializers import (
    GreenhouseMetricSerializer,
    UserSettingSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status

# Pagination Class
class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# User Registration View
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login View (Returns JWT token)
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(username=serializer.validated_data['username']).first()
            if user and user.check_password(serializer.validated_data['password']):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Logout View
class UserLogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()  # Delete token to log out
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)

# Greenhouse Metric ViewSet (CRUD with Pagination and Filtering)
class GreenhouseMetricViewSet(viewsets.ModelViewSet):
    queryset = GreenhouseMetric.objects.all()
    serializer_class = GreenhouseMetricSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['temperature', 'humidity', 'date']  # Filter by fields like temperature, humidity, or date

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# User Settings ViewSet (CRUD with Pagination and Filtering)
class UserSettingViewSet(viewsets.ModelViewSet):
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['threshold_temperature', 'threshold_humidity']  # Filter by thresholds

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
