from django.contrib import admin
from django.urls import path, include
import contactus
from contactus import views as contact_views
from django.conf.urls.static import static
from django.conf import settings
#  from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('bookingapp.urls')),
    path('contactus/', contact_views.contact_view, name='contact'),
    path('guest/', include('guestprofile.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
