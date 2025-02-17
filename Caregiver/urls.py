from django.urls import path
from .views import caregiver_data

urlpatterns = [
    path('', caregiver_data, name='caregiver_data'),  # Ensure the function `caregiver_data` exists in views.py
]
