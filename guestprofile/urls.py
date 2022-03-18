from django.urls import path
from . import views

urlpatterns = [
    path('', views.guests_profile, name='guest'),
]
