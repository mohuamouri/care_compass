#from django.urls import path
#from .views import DoctorAppointment, DoctorsAppointmentDetail  # Import views properly

urlpatterns = [
    path('doctor/', DoctorAppointment_data, name='DoctorAppointment_data'),
    path('doctor/<int:pk>/', DoctorsAppointment_data, name='DoctorsAppointment_data'),
]
