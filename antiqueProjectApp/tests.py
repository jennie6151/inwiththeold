from django.test import TestCase
from .models import Antique

class AntiqueTests(TestCase):
    
    def test_str(self):
        test_name = Antique(AntiqueName = 'AntiqueName')
        self. assertEqual(str(test_name), 'AntiqueName')

