from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class WeatherTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_weather(self):
        response = self.client.get('/api/weather/', {'city': 'Bishkek'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
