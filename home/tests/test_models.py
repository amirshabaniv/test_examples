from django.test import TestCase
from home.models import Writer
from model_bakery import baker

class TestWriterModel(TestCase):

    def setUp(self):
        self.writer = baker.make(Writer, first_name='amir', last_name='amiri')

    def test_model_str(self):
        self.assertEqual(str(self.writer), 'amir amiri')
