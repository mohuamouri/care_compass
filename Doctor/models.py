from django.db import models

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('bkash', 'bkash'),
        ('nogod', 'nogod'),
        ('rocket', 'rocket'),
        #('Other', 'other'),
    ]

    # Commented out email field to prevent null values
    # email = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, verbose_name="user", on_delete=models.CASCADE, null=True, blank=True, related_name='doctor')

    dr_name = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    degree = models.CharField(max_length=100, blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=100, help_text="Specific area of expertise")  # New field
    institute = models.CharField(max_length=100, blank=True, null=True)
    day_of_service = models.JSONField(blank=True, null=True, help_text="Days available for service (as an array)")
    time_of_service = models.CharField(max_length=255, blank=True, null=True,
                                       help_text="Time available for service (as a string)")
    mobile = models.CharField(max_length=15, blank=True, null=True, unique=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True, choices=PAYMENT_METHOD_CHOICES)
    payment_method_number = models.CharField(max_length=15, blank=True, null=True)
    nid = models.CharField(max_length=20, blank=True, null=True, unique=True)
    experience = models.PositiveIntegerField(blank=True, null=True, help_text="Years of experience")

    is_approved = models.BooleanField(default=False)  # Admin approval field

    def __str__(self):
        return f"{self.dr_name} - {self.specialty}"
