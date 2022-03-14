from django.http import HttpResponse
from django.views import generic
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from .forms import ContactForm
from bookingproject import settings


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["full_name"]}'
            message = form.cleaned_data["contacting"]
            sender = form.cleaned_data["email"]
            recipients = ['martina01061987@gmail.com']
            try:
                form.send_mail(subject, message, sender, recipients, fail_silently=True)

            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
        return render(request, 'contactus/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contactus/contact.html', context)
