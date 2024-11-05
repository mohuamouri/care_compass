from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('dr_name', 'specialty', 'gender', 'institute', 'day_of_service', 'time_of_service', 'experience')
    search_fields = ('dr_name', 'specialty', 'institute')
    list_filter = ('specialty', 'gender', 'day_of_service', 'institute')

admin.site.register(Doctor, DoctorAdmin)
