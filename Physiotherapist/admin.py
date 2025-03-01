from django.contrib import admin
from .models import Physiotherapist

class PhysiotherapistAdmin(admin.ModelAdmin):
    list_display = ('physiotherapist_name', 'gender', 'institute', 'day_of_service', 'time_of_service', 'experience', 'is_approved')  # Removed 'specialty'
    search_fields = ('physiotherapist_name', 'institute')  # Removed 'specialty'
    list_filter = ('gender', 'day_of_service', 'institute', 'is_approved')  # Removed 'specialty'

admin.site.register(Physiotherapist, PhysiotherapistAdmin)
