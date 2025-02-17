from django.contrib import admin

# Register your models here.
from django.contrib import admin

from django.contrib import admin
from .models import Pharmacy

class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('phar_name', 'owner_name', 'license_num', 'address', 'contact_num', 'email', 'opening_h', 'closing_h', 'is_approved')
    search_fields = ('phar_name', 'owner_name', 'license_num', 'address', 'email')
    list_filter = ('is_approved',)

admin.site.register(Pharmacy, PharmacyAdmin)

