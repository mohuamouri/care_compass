# Generated by Django 4.0.4 on 2025-02-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0008_remove_doctor_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_approved',
            field=models.BooleanField(default=False, verbose_name='Aprroved'),
        ),
    ]
