# Generated by Django 4.0.4 on 2025-03-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nurse', '0002_alter_nurse_day_of_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F'), ('O', 'O')], max_length=15, null=True),
        ),
    ]
