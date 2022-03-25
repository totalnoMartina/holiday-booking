from django.shortcuts import render
from .models import Apartment
from django.core.mail import send_mail
from bookingproject import settings
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
    """ A page to aquire bookings """
    pass
