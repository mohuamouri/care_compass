from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'age', 'gender', 'contact_number', 'emergency_contact', 'dr_name')
    search_fields = ('patient_name', 'contact_number')
    list_filter = ('gender', 'dr_name')

admin.site.register(Patient, PatientAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'age', 'gender', 'contact_number', 'emergency_contact', 'dr_name')
    search_fields = ('patient_name', 'contact_number')
    list_filter = ('gender', 'dr_name')

admin.site.register(Patient, PatientAdmin)
