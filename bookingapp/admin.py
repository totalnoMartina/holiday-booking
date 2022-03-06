from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Apartment, Guest, Booking, FrontPhoto, AddMorePhotos

@admin.register(Apartment)
class ApartmentAdmin(SummernoteModelAdmin):
    """ Style for admin page to have more aesthetic view """
    list_display = ('apartment_name', 'price', 'beds_nr')
    summernote_fields = ('description')


admin.site.register(Guest)
@admin.register(Booking)
class BookingRequest(admin.ModelAdmin):
    """ Add view for the admin to see booking requests """

    list_display = ('booking_num', 'apartment', 'guest_name')


@admin.register(FrontPhoto)
class ShowFrontPhoto(SummernoteModelAdmin):
    """ For admin to see which image has been uploaded """
    
    media = 'front_image'    


admin.site.register(AddMorePhotos)

