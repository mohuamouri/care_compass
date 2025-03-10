# Generated by Django 4.0.4 on 2025-03-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nurse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='day_of_service',
            field=models.JSONField(blank=True, help_text='Days available for service (as an array)', null=True),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('bkash', 'bkash'), ('nogod', 'nogod'), ('rocket', 'rocket')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='time_of_service',
            field=models.CharField(blank=True, help_text='Time available for service (as a string)', max_length=255, null=True),
        ),
    ]
