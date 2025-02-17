from django.urls import path
from .views import physiotherapist_data

urlpatterns = [
    path('', physiotherapist_data, name='physiotherapist_data'),  # Ensure the function `physiotherapist_data` exists in views.py
]
