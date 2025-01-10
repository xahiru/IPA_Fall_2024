from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from .models import GreenhouseMetric, UserSetting
from django.contrib.auth.models import User

class GreenhouseMetricTests(APITestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Generate a JWT token for the user
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)
        
        # Create a sample GreenhouseMetric instance
        self.greenhouse_metric = GreenhouseMetric.objects.create(
            temperature=22.5,
            humidity=60,
            light=300
        )
        
        # Define the URL for greenhouse metrics API
        self.url = reverse('greenhouse-metric-list')  # 'greenhouse-metric-list' corresponds to the viewset route

    def test_get_greenhouse_metrics(self):
        # Test the GET endpoint for greenhouse metrics
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['temperature'], 22.5)

    def test_post_greenhouse_metric(self):
        # Test the POST endpoint for creating a new greenhouse metric
        data = {
            'temperature': 24.0,
            'humidity': 55,
            'light': 350
        }
        response = self.client.post(self.url, data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['temperature'], 24.0)

    def test_get_metrics_export(self):
        # Test the export metrics endpoint
        export_url = reverse('export_metrics')  # This matches the export_metrics view
        response = self.client.get(export_url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

class UserSettingTests(APITestCase):
    def setUp(self):
        # Create a test user and set up authentication
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)
        
        # Create a sample UserSetting instance
        self.user_setting = UserSetting.objects.create(
            user=self.user,
            setting_name='Theme',
            setting_value='Dark'
        )
        
        # Define the URL for user settings API
        self.url = reverse('user-setting-list')  # 'user-setting-list' corresponds to the viewset route

    def test_get_user_settings(self):
        # Test the GET endpoint for user settings
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['setting_name'], 'Theme')

    def test_post_user_setting(self):
        # Test the POST endpoint for creating a new user setting
        data = {
            'setting_name': 'Language',
            'setting_value': 'English'
        }
        response = self.client.post(self.url, data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['setting_name'], 'Language')

class AuthTests(APITestCase):
    def setUp(self):
        # Create a user to test token authentication
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_token_obtain(self):
        # Test obtaining a token
        url = reverse('token_obtain_pair')
        data = {'username': 'testuser', 'password': 'password123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        # Test refreshing the token
        refresh = RefreshToken.for_user(self.user)
        url = reverse('token_refresh')
        data = {'refresh': str(refresh)}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
