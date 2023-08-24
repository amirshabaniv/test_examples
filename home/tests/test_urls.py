from django.test import TestCase
from django.urls import reverse, resolve
from home.views import Home, About

class TestUrls(TestCase):
    def test_home(self):
        url = reverse('home:home')
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_about(self):
        url = reverse('home:about', args=('amir',))
        self.assertEqual(resolve(url).func.view_class, About)