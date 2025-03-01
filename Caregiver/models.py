from django.db import models

# Create your models here.
from django.db import models

class Caregiver(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('approved', 'approved'),
    )

    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
        ('O', 'O'),
    )

    PAYMENT_METHOD_CHOICES = [
        ('bkash', 'bkash'),
        ('nogod', 'nogod'),
        ('rocket', 'rocket'),
        # ('Other', 'other'),
    ]

    caregiver_name = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True, choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, help_text="Specific area of caregiving expertise")  # Specific expertise
    nid = models.CharField(max_length=20, blank=True, null=True, unique=True)
    experience = models.PositiveIntegerField(blank=True, null=True, help_text="Years of caregiving experience")
    mobile = models.CharField(max_length=15, blank=True, null=True, unique=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True, choices=PAYMENT_METHOD_CHOICES)
    payment_method_number = models.CharField(max_length=15, blank=True, null=True)
    institute = models.CharField(max_length=100, blank=True, null=True)
    day_of_service = models.JSONField(blank=True, null=True, help_text="Days available for service (as an array)")
    time_of_service = models.CharField(max_length=255, blank=True, null=True,
                                       help_text="Time available for service (as a string)")

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')  # Updated status field
    is_approved = models.BooleanField(default=False)  # Admin approval field

    def __str__(self):
        return f"{self.caregiver_name} - {self.department}"
