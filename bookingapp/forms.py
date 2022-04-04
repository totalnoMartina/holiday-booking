from django import forms
from .models import APARTMENTS
from django.forms import ModelForm
from .models import Feedback

# 2 forms = booking(vacantapartmentsform) and guest form

class VacantApartmentsForm(forms.Form):
    chosen_apartment = forms.ChoiceField(choices=APARTMENTS, required=True)
    check_in = forms.DateField(required=True, input_formats=["%Y-%m-%dT", ])
    check_out = forms.DateField(required=True, input_formats=["%Y-%m-%dT", ])


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'How was your stay...?'})
