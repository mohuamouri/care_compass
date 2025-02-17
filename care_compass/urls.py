from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),  # Students app
    path('api/auth/', include('user.urls')),  # User app
    path('api/doctors/', include('Doctor.urls')),  # Doctors app
    path('api/nurses/', include('Nurse.urls')),  # Doctors app
    path('api/caregivers/', include('Caregiver.urls')),  # Doctors app
    path('api/physiotherapist/', include('Physiotherapist.urls')),  # Doctors app

                  # Add the /doctor/ URL here
    path('doctor/', include('Doctor.urls')),  # Assuming you want to map it to views in the Doctor app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
