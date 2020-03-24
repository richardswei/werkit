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
        self.credentials = {
            'username': 'admin',
            'password': 'admin123'
        }

    def test_login(self):
        auth_url = reverse('signin')
        response = self.client.post(auth_url, data=self.credentials, format='json')
        self.assertEqual(response.status_code, 200)

    def test_authenticated(self):
        auth_url = reverse('signin')
        auth_ping_url = reverse('auth_ping')
        response = self.client.post(auth_url, data=self.credentials, format='json')
        ping_response = self.client.get(
            auth_ping_url,
            format='json',
            HTTP_AUTHORIZATION='Token ' + response.data['token']
        )
        self.assertEqual(ping_response.status_code, 200)

    def test_no_token(self):
        auth_ping_url = reverse('auth_ping')
        ping_response = self.client.get(auth_ping_url, format='json')
        self.assertEqual(ping_response.status_code, 401)

    def test_sign_out(self):
        auth_url = reverse('signin')
        response = self.client.post(
            auth_url,
            data=self.credentials,
            format='json'
        )
        logout_url = reverse('signout')
        signout_response = self.client.delete(
            logout_url,
            format='json',
            HTTP_AUTHORIZATION='Token ' + response.data['token']
        )
        self.assertEqual(signout_response.status_code, 200)


class NotesTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.notes_url = reverse('notes')

    def test_note_post(self):
        note = {
            'title': 'title',
            'description': 'description'
        }
        self.client.force_login(user=self.user)
        self.token = Token.objects.get_or_create(user=self.user)[0].key
        response = self.client.post(self.notes_url, data=note, format='json', HTTP_AUTHORIZATION='Token ' + self.token)
        self.assertEqual(response.status_code, 201)

    def test_invalid_note_post(self):
        note = {
            'title': '',
            'description': 'description'
        }
        self.client.force_login(user=self.user)
        self.token = Token.objects.get_or_create(user=self.user)[0].key
        response = self.client.post(self.notes_url, data=note, format='json', HTTP_AUTHORIZATION='Token ' + self.token)
        self.assertEqual(response.status_code, 400)