from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('booking/', views.BookingView, name='bookings'),
]
