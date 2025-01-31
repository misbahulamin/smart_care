# Generated by Django 5.0.7 on 2024-07-18 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0007_alter_appointment_appointment_status_and_more"),
        ("doctor", "0005_alter_doctor_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="time",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="doctor.availabletime"
            ),
        ),
    ]
