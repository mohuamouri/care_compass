from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Nurse

class NurseAdmin(admin.ModelAdmin):
    list_display = ('nurse_name', 'department', 'gender', 'institute', 'day_of_service', 'time_of_service', 'experience', 'is_approved')
    search_fields = ('nurse_name', 'department', 'institute')
    list_filter = ('department', 'gender', 'day_of_service', 'institute', 'is_approved')

admin.site.register(Nurse, NurseAdmin)
