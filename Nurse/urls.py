from django.urls import path
from .views import nurse_data

urlpatterns = [
    path('', nurse_data, name='nurse_data'),  # Ensure the function `nurse_data` exists in views.py
]
