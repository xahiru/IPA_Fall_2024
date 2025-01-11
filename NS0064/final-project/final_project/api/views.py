from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from .models import GreenhouseData, UserControl
from .serializers import UserRegistrationSerializer, GreenhouseDataSerializer, UserControlSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny] 


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GreenhouseMetricsViewSet(viewsets.ModelViewSet):
    queryset = GreenhouseData.objects.all()
    serializer_class = GreenhouseDataSerializer
    permission_classes = [IsAuthenticated]

    # Optional action for additional functionality (e.g., filtering, or custom methods)
    @action(detail=False, methods=['get'])
    def latest(self, request):
        latest_metrics = GreenhouseData.objects.last()
        serializer = self.get_serializer(latest_metrics)
        return Response(serializer.data)


class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserControl.objects.all()
    serializer_class = UserControlSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Return settings for the currently authenticated user
        return UserControl.objects.get(user=self.request.user)