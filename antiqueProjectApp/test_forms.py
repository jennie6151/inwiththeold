from django.test import TestCase
from .forms import AntiquePurchaseForm
from antiqueProjectApp.models import Antique

# Create your tests here.
class TestAntiquePurchaseForm(TestCase):
#Test to check that the payment form cannot be submitted by just customerFirstName
    def test_cannot_make_a_payment_with_just_a_name(self):
        form = AntiquePurchaseForm({'customerFirstName': 'Create Tests'})
        self.assertFalse(form.is_valid())

#Test to check that the payment form can only be submitted if all fields are complete
    def test_can_only_make_a_payment_with_all_details(self):
        Antique.objects.create(AntiqueName='Test')
        pk=Antique.objects.get(AntiqueName='Test').pk
        form = AntiquePurchaseForm({'antique':pk, 'customerFirstName': 'Create Tests', 'customerLastName': 'Create Tests', 'customerAddressLine1': 'Create Tests', 'customerAddressLine2': 'Create Tests', 'customerAddressCity': 'Create Tests', 'customerAddressCounty': 'Create Tests', 'customerAddressPostcode': 'Create Tests', 'customerEmail': 'Create Tests', 'customerTelephone': 'Create Tests'})
        self.assertTrue(form.is_valid())

