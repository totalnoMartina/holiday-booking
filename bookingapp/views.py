from django.shortcuts import render
from .models import Apartment
# from django.views import generic


def home(request):
    """ A view to return the homepage """

    return render(request, 'bookingapp/index.html')

def apartments(request):
    """ A page to view apartments """
    apartments = Apartment.objects.all()

    template = 'bookingapp/apartments.html'
    context = {
        'apartments': apartments,
        # 'front_image': front_image
    }
    return render(request, template, context)

def booking(request):
    """ A page to view apartments """
    return render(request, 'bookingapp/booking_page.html')
