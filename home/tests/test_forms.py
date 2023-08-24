from django.test import TestCase
from home.forms import UserRegistrationForm
from django.contrib.auth.models import User


class TestRegistertrationForm(TestCase):

    def setUp(self):
        User.objects.create_user(username='kevin',
                                 email='kevin@gmail.com',
                                 password='kevin')
        
    def test_valid_data(self):
        form = UserRegistrationForm(data={
            'username':'amir',
            'email':'amir@gmail.com',
            'password1':'amir',
            'password2':'amir'
        })
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_exist_email(self):
        form = UserRegistrationForm(data={
            'username':'k',
            'email':'kevin@gmail.com',
            'password1':'k',
            'password2':'k'
        })
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))

    def test_unmatche_password(self):
        form = UserRegistrationForm(data={
            'username':'a',
            'email':'a@gmail.com',
            'password1':'a1',
            'password2':'a2'
        })
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error)