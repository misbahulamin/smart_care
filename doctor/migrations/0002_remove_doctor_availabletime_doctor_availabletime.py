# Generated by Django 5.0.7 on 2024-07-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="AvailableTime",
        ),
        migrations.AddField(
            model_name="doctor",
            name="AvailableTime",
            field=models.ManyToManyField(to="doctor.availabletime"),
        ),
    ]
