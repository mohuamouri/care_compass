from django.urls import path
from .views import doctor_data

urlpatterns = [
    path('', doctor_data, name='doctor_data'),  # Ensure the function `doctor_data` exists in views.py

]
