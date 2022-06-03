from django.test import TestCase
from django.urls import reverse
from rest_framework import status
class TestSnackView(TestCase):

    def setUp(self):
        self.client.login(username="testuser", password="qpal1029")
    
    def test_authetication_required(self):
        self.client.logout()
        url = reverse('snacks-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
