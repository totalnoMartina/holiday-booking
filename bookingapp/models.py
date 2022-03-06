import uuid

from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

# Models for Guest, Booking, Apartment

class Guest(models.Model):
    """ Attributes of class Guest """
    guest_id = models.CharField(max_length=50, blank=False, primary_key=True)
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
    apartment_name = models.CharField(choices=APARTMENTS, max_length=10, primary_key=True)
    beds_nr = models.IntegerField()
    kitchen = models.BooleanField(default=True,name='kitchen')
    balcony = models.BooleanField(default=True, name='balcony')
    seaview = models.BooleanField(default=True, name='seaview')
    air_cond = models.BooleanField(default=True, name='AC')
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    description = models.TextField(name='description', null=True)

    

    def __str__(self):
        """ Showing apartment class model created """
        return f'An apartment named {self.apartment_name} with {self.beds} beds and the price of {self.price} euros is created'


class FrontPhoto(models.Model):
    """ A class for the front image """
    front_img = CloudinaryField('front_image')
    related_to_apartment = models.ForeignKey(Apartment,
                            on_delete=models.CASCADE)

    def __str__(self):
        return f'Image uploaded to apartment {self.related_to_apartment}'

class AddMorePhotos(models.Model):
    """ A class to add more photos """
    add_images = CloudinaryField('more_images')
    related_to_apartment = models.ForeignKey(Apartment,
                            on_delete=models.CASCADE)
    related_to_front_img = models.ForeignKey(FrontPhoto,
                            on_delete=models.CASCADE)

    def __str__(self):
        return f' Uploaded succesfully, for {self.related_to_apartment} apartment'

class Booking(models.Model):
    """ A class to contain booking attributes and methods """
    booking_num = models.CharField(max_length=32, null=False, editable=False, primary_key=True)
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_created_on = models.DateTimeField(auto_now_add=True)

    def _generate_booking_num(self):
        """
        Used to generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save_booking_num(self):
        """  """
        self.booking_num = self._generate_order_number()
        super().save(*args, **kwargs)

    
