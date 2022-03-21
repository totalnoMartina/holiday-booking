from django.shortcuts import render, get_object_or_404
from .models import GuestProfile

def guests_profile(request):
    """ Display the guests profile """
    profile = get_object_or_404(GuestProfile, guest=request.user)
    template = 'guestprofile/guest.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)
