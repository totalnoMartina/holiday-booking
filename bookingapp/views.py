from django.shortcuts import render
from .models import Apartment
from bookingapp.forms import BookContact
from django.core.mail import send_mail
from bookingproject import settings
import sendgrid
import os
# using SendGrid's Python Library


# from django.views import generic


def home(request):
    """ A view to return the homepage """
    apartments = Apartment.objects.all()
    template = 'bookingapp/index.html'
    context = {
        'apartments': apartments,
    }

    return render(request, template, context)

def apartments(request):
    """ A page to view apartments """
    apartments = Apartment.objects.all()
    template = 'bookingapp/apartments.html'
    context = {
        'apartments': apartments,
    }

    return render(request, template, context)


def booking_contact(request):
    """ A page to send email to aquire bookings """

    submitSent = False
    if request.method == 'GET':
        form = BookContact()
    else:
        form = BookContact(request.POST)
        if form.is_valid():
            sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
            cd = form.cleaned_data
            full_name = cd['full_name']
            from_email = cd['email']
            new_contact = cd['contacting']
            send_mail(full_name, new_contact, from_email, ['martina01061987@gmail.com',cd['email'], ])
            response = sg.send(request_body=mail.get())
            submitSent = True
        else:
            form = BookContact()
    return render(request, 'bookingapp/booking_page.html',
                {'form': form,
                'submitSent' : submitSent
                })
