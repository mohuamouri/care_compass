from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialization', 'gender', 'degree', 'institute', 'day_of_service', 'time_of_service', 'mobile', 'is_approved')

# Only register if Doctor is not already registered
if not admin.site.is_registered(Doctor):
    admin.site.register(Doctor, DoctorAdmin)
