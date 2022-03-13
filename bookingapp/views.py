from django.shortcuts import render
from .models import Apartment
from bookingapp.forms import BookContact
from django.core.mail import send_mail
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
    if request.method == 'GET':
        form = BookContact()
    else:
        form = BookContact(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            from_email = form.cleaned_data['from_email']
            new_contact = form.cleaned_data['contact-us']
            send_mail(subject, message, from_email, ['martina01061987@gmail.com'])

    return render(request, 'bookingapp/booking_page.html', {'form': form})


