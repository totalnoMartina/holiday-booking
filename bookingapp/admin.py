from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Apartment, Guest, Booking, FrontPhoto, AddMorePhotos

@admin.register(Apartment)
class ApartmentAdmin(SummernoteModelAdmin):

    list_display = ('apartment_name', 'price', 'beds_nr')
    summernote_fields = ('apartment_name', 'price', 'description')


admin.site.register(Guest)

@admin.register(Booking)
class BookingRequest(admin.ModelAdmin):

    list_display = ('booking_num', 'apartment', )

admin.site.register(FrontPhoto)
admin.site.register(AddMorePhotos)
