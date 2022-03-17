from django.shortcuts import render

def guests_profile(request):
    """ Display the guests profile """
    template = 'guestprofile/guest.html'
    context = {}

    return render(request, template, context)
