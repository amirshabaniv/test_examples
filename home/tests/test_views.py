from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from home.forms import UserRegistrationForm
from home.views import Home



class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('home:user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/register.html')
        self.failUnless(response.context['form'], UserRegistrationForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('home:user_register'), data={'username':'a', 'email':'a@gmail.com', 'password1':'a', 'password2':'a'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))
        self.assertEqual(User.objects.count(), 1)

    def test_user_register_POST_invalid(self):
        response = self.client.post(reverse('home:user_register'), data={'username':'jack', 'email':'invalid_email', 'password1':'jack', 'password2':'jack'})
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(form=response.context['form'], field='email', errors=['Enter a valid email address.'])


class TestWriterView(TestCase):

    def setUp(self):
        User.objects.create_user(username='root', email='root@email.com', password='root')
        self.client = Client()
        self.client.login(username='root', email='root@email.com', password='root')

    def test_writers(self):
        response = self.client.get(reverse('home:writers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/writers.html')


class TestHomeView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='root', email='root@gmail.com', password='root')
        self.factory = RequestFactory()

    def test_home_user_authenticated(self):
        request = self.factory.get(reverse('home:home'))
        request.user = self.user
        response = Home.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_home_user_anonymous(self):
        request = self.factory.get(reverse('home:home'))
        request.user = AnonymousUser()
        response = Home.as_view()(request)
        self.assertEqual(response.status_code, 200)