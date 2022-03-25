from django.shortcuts import render
from django.views.generic import FormView
from .models import Apartment
from django.core.mail import send_mail
from bookingproject import settings
from .forms import VacantApartmentsForm

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


class BookingView(FormView):
    form_class = VacantApartmentsForm
    template_name = 'apartments_vacant.html'

    def form_valid(self, form):
        data = form.cleaned_data
        apartments_list = Apartment.objects.filter()
