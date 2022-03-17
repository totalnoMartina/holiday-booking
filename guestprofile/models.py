import uuid
from django.db import models
from django.core.validators import RegexValidator  # For formatting the phone number
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class GuestProfile(models.Model):
    """ Attributes of class Guest """
    guest = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False)
    ph_number = models.CharField(null=False, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')], max_length=40)
    email = models.EmailField(blank=False)
    kids = models.BooleanField(default=False, blank=True)
    pets = models.BooleanField(default=False, blank=True)

    def __str__(self):
        """ A method to show stored data of Guest """
        return f'A guest with an id of {self.guest_id},  {self.full_name} with a phone number: {self.ph_number} has been created! Welcome {self.guest}'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update user profile """
    if created:
        GuestProfile.objects.create(guest=instance)
    #  Existing users just save the profile
    instance.guestprofile.save()
