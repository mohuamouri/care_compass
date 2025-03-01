# Generated by Django 4.0.4 on 2025-03-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0015_remove_doctor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='day_of_service',
            field=models.JSONField(blank=True, help_text='Days available for service (as an array)', null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Bkash', 'Bkash'), ('Nogod', 'Nogod'), ('Rocket', 'Rocket')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='time_of_service',
            field=models.CharField(blank=True, help_text='Time available for service (as a string)', max_length=255, null=True),
        ),
    ]
