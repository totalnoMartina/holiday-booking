from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('booking_page/', views.booking, name='bookings'),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('feedback/', views.feedbacks, name='feedback'),

]
