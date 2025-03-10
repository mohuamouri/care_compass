# Generated by Django 4.0.4 on 2025-02-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurse_name', models.CharField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=15, null=True)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(help_text='Specific area of expertise', max_length=100)),
                ('nid', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('experience', models.PositiveIntegerField(blank=True, help_text='Years of experience', null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('payment_method', models.CharField(blank=True, choices=[('Cash', 'cash'), ('Card', 'card'), ('Online Transfer', 'online Transfer'), ('Other', 'other')], max_length=20, null=True)),
                ('PAYMENT_METHOD_CHOICES', models.CharField(blank=True, max_length=15, null=True)),
                ('institute', models.CharField(blank=True, max_length=100, null=True)),
                ('day_of_service', models.CharField(blank=True, help_text='Day(s) available for service', max_length=20, null=True)),
                ('time_of_service', models.PositiveIntegerField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
