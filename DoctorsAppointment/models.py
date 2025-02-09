from django.db import models
from django.utils.timezone import now
from Doctor.models import Doctor
from django.core.validators import RegexValidator


STATUS_CHOICES = (
    ('pending', 'pending'),
    ('cancelled', 'cancelled'),
    ('completed', 'completed'),
    ('approved', 'approved'),
)

#PAYMENT_CHOICES = (
#    ('unpaid', 'unpaid'),
#    ('pending', 'pending'),
#    ('paid', 'paid'),
#)

#PAYMENT_METHOD = (
#    ('Bkash', 'Bkash'),
#    ('Nogod', 'Nogod'),
#    ('Rocket', 'Rocket'),
#    ('Upay', 'Upay'),
#)


class DoctorsAppointment(models.Model):
    # If you want to relate to a patient model, uncomment this line and define the model correctly
    # patient_name = models.ForeignKey(patient, verbose_name="patient", on_delete=models.CASCADE, null=True, blank=True, related_name='appointments')

    patient_name = models.CharField(max_length=255, default="Unknown")
    patient_age = models.PositiveIntegerField()  # Use IntegerField for age
    patient_phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')]  # A simple phone number validator
    )
    type = models.CharField(max_length=120)
    fee = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField for fee
    dr_name = models.ForeignKey(
        Doctor, verbose_name="Doctor", on_delete=models.CASCADE, null=True, blank=True, related_name='appointments')

    date = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)
   # payment_method = models.CharField(
       # max_length=120, choices=PAYMENT_METHOD, default="Bkash")
   # transaction_id = models.CharField(max_length=120, null=True, blank=True)
   # payment_status = models.CharField(
    #    max_length=120, choices=PAYMENT_CHOICES, default="unpaid")
    service_status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="approved")
    details = models.TextField()

    class Meta:
        verbose_name_plural = "Doctors Appointment"

    def __str__(self):
        return f"Appointment with Dr. {self.dr_name} for {self.patient_name}"
