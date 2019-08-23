from django import forms
from antiqueProjectApp.models import AntiqueSale


class AntiquePurchaseForm(forms.ModelForm):
    class Meta:
        model = AntiqueSale
        fields = ('antique', 'customerFirstName', 'customerLastName', 'customerAddressLine1', 'customerAddressLine2',
                  'customerAddressCity', 'customerAddressCounty', 'customerAddressPostcode', 'customerEmail', 'customerTelephone')
        widgets = {'antique': forms.HiddenInput()}
        labels = {
            'customerFirstName': 'First name*', 'customerLastName': 'Last name*', 'customerAddressLine1': 'Address line 1*', 'customerAddressLine2': 'Address line 2', 'customerAddressCity': 'City*', 'customerAddressCounty': 'County*', 'customerAddressPostcode': 'Postal code*', 'customerEmail': 'Email address*', 'customerTelephone': 'Telephone number*',
        }
