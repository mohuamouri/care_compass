# Generated by Django 4.0.4 on 2025-01-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0005_remove_doctor_user_doctor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='time_of_service',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
