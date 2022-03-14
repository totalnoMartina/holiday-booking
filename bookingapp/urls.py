from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from contactus import views as contact_views


urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('contactus/', contact_views.contact_view, name='contact')
] + staticfiles_urlpatterns()
