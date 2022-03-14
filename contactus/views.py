from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from bookingproject import settings


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['contacting']
            send_mail(email_subject, email_message, form.cleaned_data["email"], settings.ADMIN_EMAIL)
            return render(request, 'contactus/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contactus/contact.html', context)