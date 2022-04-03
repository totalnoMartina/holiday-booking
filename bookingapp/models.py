import uuid
import datetime
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField
from django_google_maps import fields as map_fields
from guestprofile.models import GuestProfile

# Models for Guest, Booking, Apartment



class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)


class Guest(models.Model):
    """ Attributes of class Guest """
    guest = models.CharField(max_length=50, blank=False, primary_key=True)
    full_name = models.CharField(max_length=100, blank=False)
    ph_number = models.CharField(null=False, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')], max_length=40)
    email = models.EmailField(blank=False)
    kids = models.BooleanField(default=False, blank=True)
    pets = models.BooleanField(default=False, blank=True)

    def __str__(self):
        """ A method to show stored data of Guest """
        return f'A guest with an id of {self.guest_id},  {self.full_name} with a phone number: {self.ph_number} has been created!'


APARTMENTS = (('Tony', 'Tony Apartment for max4 people'),
                ('Matea', 'Matea apartment for max4 people'),
                ('Martina', 'Martina apartment for max6 people'))


class Apartment(models.Model):
    """ A class to create an apartment in offer """
    guest_profile = models.ForeignKey(GuestProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='GuestProf')
    apartment_name = models.CharField(choices=APARTMENTS, max_length=10, primary_key=True)
    beds_nr = models.IntegerField()
    kitchen = models.BooleanField(default=True,name='kitchen')
    balcony = models.BooleanField(default=True, name='balcony')
    seaview = models.BooleanField(default=True, name='seaview')
    air_cond = models.BooleanField(default=True, name='AC')
    front_image = CloudinaryField('front_image', default='first_img')  # cloudinary needs to store this
    front_image2 = CloudinaryField('front_image2', default='second_img')  # cloudinary needs to store this
    front_image3 = CloudinaryField('front_image3', default='third_img')  # cloudinary needs to store this
    front_image4 = CloudinaryField('front_image4', default='third_img')  # cloudinary needs to store this
    front_image5 = CloudinaryField('front_image5', default='third_img')  # cloudinary needs to store this
    front_image6 = CloudinaryField('front_image6', default='third_img')  # cloudinary needs to store this
    front_image7 = CloudinaryField('front_image7', default='third_img')  # cloudinary needs to store this
    front_image8 = CloudinaryField('front_image8', default='third_img')  # cloudinary needs to store this
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    description = models.TextField(name='description', null=True)

    def __str__(self):
        """ Showing apartment class model created """
        return f'An apartment named {self.apartment_name} with {self.beds_nr} beds and the price of {self.price} euros is created'


# Helper constant variables for indicating time

DURATION_ZERO = datetime.time(hour=0)
DEFAULT_DURATION = datetime.time(hour=1)
DEFAULT_TIME = datetime.time(hour=12)

# A code and a validator that helps present field like a numeric pad
phoneValidator = RegexValidator(
    regex=r'[0-9][0-9 ]+',
    message='Not a valid phone number')


class Booking(models.Model):
    """ A class to contain booking attributes and methods """
    booking_num = models.CharField(max_length=32, null=False, editable=False, primary_key=True)
    guest_name = models.ForeignKey(Guest, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_created_on = models.DateTimeField(auto_now_add=True)
    booking_approved = models.BooleanField(default=False)

    def _generate_booking_num(self):
        """
        Used to generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save_booking_num(self):
        """ Used to save the booking number as random chosen number """
        self.booking_num = self._generate_booking_num()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.apartment} is booked for {self.guest_name}, with the ID of {self.booking_num}'


class Feedback(models.Model):
    """ Guests who are logged in and have visited
    can give feedback about their stay """
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Feedback #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'feedback'
