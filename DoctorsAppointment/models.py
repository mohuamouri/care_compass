from django.db import models
from django.utils.timezone import now
from Doctor.models import Doctor
#from patient.models import patient



# Create your models here.
STATUS_CHOICES = (
    ('pending', 'pending'),
    ('cancelled', 'cancelled'),
    ('completed', 'completed'),
    ('approved', 'approved'),
)
PAYMENT_CHOICES = (
    ('unpaid', 'unpaid'),
    ('pending', 'pending'),
    ('paid', 'paid'),
)
PAYMENT_METHOD = (
    ('Bkash', 'Bkash'),
    ('Nogod', 'Nogod'),
    ('Rocket', 'Rocket'),
    ('Upay', 'Upay'),
)


class DoctorsAppointment(models.Model):
    #patient_name = models.ForeignKey(
        #patient, verbose_name="patient", on_delete=models.CASCADE, null=True, blank=True, related_name='appointment')

    patient_age = models.CharField(max_length=120)
    patient_phone = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    fee = models.CharField(max_length=120)
    dr_name = models.ForeignKey(
        Doctor, verbose_name="Doctor", on_delete=models.CASCADE, null=True, blank=True , related_name='appointment' )

    date = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)
    payment_method = models.CharField(
        max_length=120, choices=PAYMENT_METHOD, default="Bkash", )
    transaction_id = models.CharField(max_length=120, null=True, blank=True)
    payment_status = models.CharField(
        max_length=120, choices=PAYMENT_CHOICES, default="unpaid", )
    service_status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="approved", )
    details = models.TextField()

    class Meta:
        verbose_name_plural = "Doctors Appointment"