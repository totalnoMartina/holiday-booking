from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Contact


class ContactForm(ModelForm):
    """ A form to use to send emails """
    full_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    contacting = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = '__all__'


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')
