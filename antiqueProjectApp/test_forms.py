from django.test import TestCase
from .forms import AntiquePurchaseForm

# Create your tests here.
class TestAntiquePurchaseForm(TestCase):

    def test_can_make_a_payment_with_just_a_name(self):
        form = AntiquePurchaseForm({'customerFirstName': 'Create Tests'})
        self.assertTrue(form.is_valid())
        