from django.contrib import admin
import json
from django_summernote.admin import SummernoteModelAdmin
from .models import Apartment, Guest, Booking, Rental, Feedback
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

@admin.register(Apartment)

class ApartmentAdmin(SummernoteModelAdmin):
    """ Style for admin page to have more aesthetic view """
    list_display = ('apartment_name', 'price', 'beds_nr')
    summernote_fields = ('description')


admin.site.register(Guest)
class GuestView(admin.ModelAdmin):
    """ Add view for the admin to see booking requests """

    list_display = ('full_name', 'email', 'ph_number')


@admin.register(Booking)

# class booking(admin.ModelAdmin):
#     """ Add view for the admin to see booking requests """

#     list_display = ('booking_num',
#                     'apartment',
#                     'guest_name',
#                     'check_in',
#                     'check_out',
#                     'booking_created_on',
#                     'booking_approved')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    """ Model for class google maps """
    formfield_overrides = {
        map_fields.AddressField: { 'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'satellite'
      })
    },
}


@admin.register(Feedback)
class FeedbackView(SummernoteModelAdmin):
    """ A dislay to see the feedback text and guest who wrote it """
    list_display = ('text', )

