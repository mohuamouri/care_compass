from django.db import models
from Doctor.models import Doctor

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    patient_name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    current_medication = models.TextField(blank=True, null=True)
    dr_name = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name="patients")

    def __str__(self):
        return self.patient_name