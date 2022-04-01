from django.shortcuts import render
from django.views.generic import FormView
from .models import Apartment
from django.core.mail import send_mail
from bookingproject import settings
from .forms import VacantApartmentsForm


def home(request):
    """ A view to return the homepage """
    template_home = 'bookingapp/index.html'

    return render(request, template_home)


def apartments(request):
    """ A page to view apartments """
    apartments = Apartment.objects.all()
    template = 'bookingapp/apartments.html'
    context = {
        'apartments': apartments,
    }

    return render(request, template, context)


def booking(request):

    template_book = 'bookingapp/booking_page.html'

    return render(request, template_book)
