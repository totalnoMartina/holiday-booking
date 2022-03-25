from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from bookingproject import settings
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["full_name"]}'
            message = form.cleaned_data["contacting"]
            sender = form.cleaned_data["email"]
            recipients = [settings.EMAIL_HOST_USER,]
            try:
                send_mail(subject, message, sender, recipients, fail_silently=False)
                messages.success(request, 'Success!')
                context = {'form': form}
                return render(request, 'contactus/success.html', context)
            except BadHeaderError():
                return HttpResponse('Invalid request!')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contactus/contact.html', context)

