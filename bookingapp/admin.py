from django.contrib import admin
from .models import Apartment, Guest, Booking, FrontPhoto, AddMorePhotos

admin.site.register(Apartment)
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(FrontPhoto)
admin.site.register(AddMorePhotos)
