from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    contacting = models.TextField()

    def __str__(self):
        return self.email
        
