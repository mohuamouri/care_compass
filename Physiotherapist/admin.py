from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Physiotherapist

class PhysiotherapistAdmin(admin.ModelAdmin):
    list_display = ('physiotherapist_name', 'specialty', 'gender', 'institute', 'day_of_service', 'time_of_service', 'experience', 'is_approved')
    search_fields = ('physiotherapist_name', 'specialty', 'institute')
    list_filter = ('specialty', 'gender', 'day_of_service', 'institute', 'is_approved')

admin.site.register(Physiotherapist, PhysiotherapistAdmin)
