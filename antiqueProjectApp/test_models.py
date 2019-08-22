from django.test import TestCase
from .forms import AntiquePurchaseForm
from antiqueProjectApp.models import Antique

class TestAntique(TestCase):
#Test to check that the price of an item is correctly multiplied by 100
    def test_price_is_correct_when_times_100(self):
        antique = Antique(Price=10.00)
        self.assertEqual(antique.price_in_pence(), antique.Price*100)
        self.assertNotEqual(antique.price_in_pence(),10)