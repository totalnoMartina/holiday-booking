from django import forms
from .models import APARTMENTS


class VacantApartmentsForm(forms.Form):
    chosen_apartment = forms.ChoiceField(choices=APARTMENTS, required=True)
    check_in = forms.DateField(required=True, input_formats=["%Y-%m-%dT", ])
    check_out = forms.DateField(required=True, input_formats=["%Y-%m-%dT", ])
