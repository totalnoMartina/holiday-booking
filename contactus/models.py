from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=False)
    contacting = models.TextField(blank=False)

    def __str__(self):
        return self.email
        
