from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterUserAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)

class LogoutUserAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
    from rest_framework.viewsets import ModelViewSet
from .models import GreenhouseMetric, UserThreshold
from .serializers import GreenhouseMetricSerializer, UserThresholdSerializer
from rest_framework.permissions import IsAuthenticated

class GreenhouseMetricViewSet(ModelViewSet):
    queryset = GreenhouseMetric.objects.all()
    serializer_class = GreenhouseMetricSerializer
    permission_classes = [IsAuthenticated]

class UserThresholdViewSet(ModelViewSet):
    queryset = UserThreshold.objects.all()
    serializer_class = UserThresholdSerializer
    permission_classes = [IsAuthenticated]