''' Urls configuration for the contact app '''

from django.urls import path
from . import views


# empty path to indicate the root url
urlpatterns = [
    path('', views.contact_view, name='contact_us'),
]