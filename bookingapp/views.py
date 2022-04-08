from django.shortcuts import render, redirect
from django.views.generic import FormView, View, ListView
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
    form_class = VacantApartmentsForm
    template_name = 'holidayapp/booking_page.html'

    def form_valid(self, form):
        data = form.cleaned_data
        apartment_list = Apartment.objects.filter(apartment_name=data['apartment_name'])
        available_aparts = []
        for apartment in apartment_list:
            # if check_if_available(apartment, data['check_in'], data['check_out']):
            #     available_aparts.append(apartment)

            if len(available_aparts) > 0:
                apartment = available_aparts[0]
                booking = Booking.objects.create(
                    user=self.request.user,
                    apartment=apartment,
                    check_in=data['check_in'],
                    check_out=data['check_out']
                )
                booking.save()
                return HttpResponse(booking)
            else:
                return HttpResponse('This apartment is already booked, please try another one')
        return HttpResponse('The apartment is booked')




        # template_book = 'bookingapp/booking_page.html'
    # if req == post
    # use both forms - guest and booking
    # if both forms valid save.forms - both
    # form action in jinja name reference of url

    def add_booking(self):
        """ A function to add bookings with times booked and app name """
        pass

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

class RoomListView(ListView):
    apartment = Apartment

class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        apartment_name = self.kwargs.get('apartment_name', None)
        form = VacantApartmentsForm()
        room_list = Apartment.objects.filter(apartment_name=apartment_name)

        if len(room_list) > 0:
            apartment = room_list[0]
            apartment_name = dict(apartment.APARTMENTS).get(apartment.apartment_name, None)
            context = {
                'apartment_name': apartment_name,
                'form': form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        apartment_name = self.kwargs.get('apartment_name', None)
        room_list = Apartment.objects.filter(apartment_name=apartment_name)
        form = VacantApartmentsForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for apartment in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            apartment = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                apartment=apartment,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')


