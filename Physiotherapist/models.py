from django.db import models

# Create your models here.
from django.db import models

class Physiotherapist(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('approved', 'approved'),
    )

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    )

    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'cash'),
        ('Card', 'card'),
        ('Online Transfer', 'online Transfer'),
        ('Other', 'other'),
    ]

    physiotherapist_name = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True, choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    specialty = models.CharField(max_length=100, help_text="Area of specialization")  # Specific expertise in physiotherapy
    nid = models.CharField(max_length=20, blank=True, null=True, unique=True)
    experience = models.PositiveIntegerField(blank=True, null=True, help_text="Years of experience in physiotherapy")
    mobile = models.CharField(max_length=15, blank=True, null=True, unique=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True, choices=PAYMENT_METHOD_CHOICES)
    payment_method_number = models.CharField(max_length=15, blank=True, null=True)  # For storing payment method number
    institute = models.CharField(max_length=100, blank=True, null=True)
    day_of_service = models.CharField(max_length=20, blank=True, null=True, help_text="Day(s) available for service")
    time_of_service = models.PositiveIntegerField(blank=True, null=True)

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')  # Updated status field
    is_approved = models.BooleanField(default=False)  # Admin approval field

    def __str__(self):
        return f"{self.physiotherapist_name} - {self.specialty}"
