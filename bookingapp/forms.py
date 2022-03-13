from django import forms


class BookContact(forms.form):
    """ A form to contact or book an apartment """
    f_name = forms.CharField()
    email = forms.EmailField(required=True)
    contacting = forms.CharField(required=True)
