from django.contrib import admin
from .models import Students
# Register your models here.


class StudentsAdmin(admin.ModelAdmin):
    list_display = ["StudentID", "Name", "Dept", "DOB", "Image"]

    class Meta:
        model = Students


admin.site.register(Students, StudentsAdmin)
