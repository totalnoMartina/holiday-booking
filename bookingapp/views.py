from django.shortcuts import render
# from django.views import generic


def home(request):
    """ A view to return the homepage """

    return render(request, 'bookingapp/index.html')
