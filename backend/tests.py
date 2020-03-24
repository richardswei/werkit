from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse


class AuthenticationTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')

    def test_login(self):
        auth_url = reverse('signin')
        credentials = {
            'username': 'admin',
            'password': 'admin123'
        }
        response = self.client.post(auth_url, data=credentials, format='json')
        self.assertEqual(response.status_code, 200)

    def test_authenticated(self):
        auth_url = reverse('signin')
        auth_ping_url = reverse('auth_ping')
        credentials = {
            'username': 'admin',
            'password': 'admin123'
        }
        response = self.client.post(auth_url, data=credentials, format='json')
        ping_response = self.client.get(auth_ping_url, format='json', HTTP_AUTHORIZATION='Token ' + response.data['token'])
        self.assertEqual(ping_response.status_code, 200)
