from django.shortcuts import render
# from django.views import generic


def home(request):
    """ A view to return the homepage """

    return render(request, 'bookingapp/index.html')

def apartments(request):
    """ A page to view apartments """
    
    return render(request, 'bookingapp/apartments.html')

def booking(request):
    """ A page to view apartments """
    return render(request, 'bookingapp/booking_page.html')
