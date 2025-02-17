from django.db import models

class Pharmacy(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    )

    phar_name = models.CharField(max_length=500, blank=True, null=True)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    license_num = models.CharField(max_length=50, blank=True, null=True, unique=True)
    address = models.CharField(max_length=100, help_text="Specific area")  # New field

    contact_num = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)

    opening_h = models.TimeField(blank=True, null=True)
    closing_h = models.TimeField(blank=True, null=True)

    is_approved = models.BooleanField(default=False)  # Admin approval field

    def __str__(self):
        return f"{self.phar_name} - {self.address}"
