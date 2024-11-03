from django.db import models

# Create your models here.
def upload_image(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Students(models.Model):
    StudentID = models.CharField(max_length=60)
    Name = models.CharField(max_length=60)
    Dept = models.CharField(max_length=60)
    DOB = models.DateField()
    Image = models.ImageField(
        upload_to=upload_image, null=True)

    class Meta:
        verbose_name_plural = "Students"
        db_table = "students"

    
