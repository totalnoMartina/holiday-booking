from django.contrib import admin
from django.urls import path, include
from contactus import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('bookingapp.urls')),
    path('contactus/', contact_views.contact_view, name='contact')
]
