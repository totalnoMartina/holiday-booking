from django import forms


class BookContact(forms.Form):
    """ A form to contact or book an apartment """
    full_name = forms.CharField()
    email = forms.EmailField(required=True)
    contacting = forms.CharField( widget=forms.Textarea, required=True)
