from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('booking/', views.booking, name='booking'),
]
