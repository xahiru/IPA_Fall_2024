from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import GreenHouseMetric

class GreenHouseMetricTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_create_metric(self):
        data = {
            'temperature': 25.0,
            'humidity': 60.0,
            'soil_moisture': 40.0,
            'light_level': 1000.0
        }
        response = self.client.post('/api/metrics/', data)
        self.assertEqual(response.status_code, 201)