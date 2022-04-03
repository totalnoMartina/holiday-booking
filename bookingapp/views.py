from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib import messages
from .models import Apartment, Feedback
from django.core.mail import send_mail
from bookingproject import settings
from .forms import VacantApartmentsForm, FeedbackForm


def home(request):
    """ A view to return the homepage """
    template_home = 'bookingapp/index.html'
    return render(request, template_home)


def apartments(request):
    """ A page to view apartments """
    apartments = Apartment.objects.all()
    feedbacks = Feedback.objects.order_by('-date_posted')

    template = 'bookingapp/apartments.html'
    context = {
        'apartments': apartments,
        'feedbacks': feedbacks,
    }
    return render(request, template, context)


def booking(request):
    """ Function to handle bookings """
    template_book = 'bookingapp/booking_page.html'
    return render(request, template_book)


def get_total_days(Booking):
    """ A function to get total number of days booked """
    start = Booking.start_date.datetime.strftime("%m/%d/%Y")
    end = Booking.end_date.datetime.strftime("%m/%d/%Y")
    total_days = end - start
    return total_days


def get_total_price(Booking):
    """ A method used to get total price """
    total_price = Booking.total_days * Apartment.price
    return f'{Booking.apartment} is booked for {Booking.guest_name}, with the ID of {Booking.booking_num} for the total of {total_price} for {Booking.total_days} days'


def feedbacks(request):
    """ A posting of feedback for guests """
    feedbacks = Feedback.objects.order_by('-date_posted')
    context = {        
        'feedbacks': feedbacks

    }
    return render(request, 'bookingapp/feedback.html', context)


def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback submitted successfully')
            return redirect('home')
    else:
        form = FeedbackForm()
    context = {'form': form}

    return render(request, 'bookingapp/add_feedback.html', context)
