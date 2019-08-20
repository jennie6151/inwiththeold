from django import forms
from antiqueProjectApp.models import AntiqueSale

class AntiquePurchaseForm(forms.ModelForm):
    class Meta:
        model = AntiqueSale
        fields = ('customerFirstName', 'customerLastName', 'customerAddressLine1', 'customerAddressLine2',
                  'customerAddressCity', 'customerAddressCounty', 'customerAddressPostcode', 'customerEmail', 'customerTelephone')
