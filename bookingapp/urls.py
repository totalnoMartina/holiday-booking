from django.urls import path
from . import views
from contactus import views as contact_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('contactus/', contact_views.contact_view, name='contact')
]
