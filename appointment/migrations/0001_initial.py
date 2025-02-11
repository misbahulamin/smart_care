# Generated by Django 5.0.7 on 2024-07-17 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("doctor", "0004_alter_review_doctor"),
        ("patient", "0002_alter_patient_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "appointment_types",
                    models.IntegerField(choices=[("1", "Offline"), ("2", "Online")]),
                ),
                (
                    "appointment_status",
                    models.IntegerField(
                        choices=[("1", "Completed"), ("2", "Pending"), ("3", "Runing")],
                        default="Pending",
                    ),
                ),
                ("symptom", models.TextField()),
                ("cancel", models.BooleanField(default=False)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doctor.doctor"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
                (
                    "time",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctor.availabletime",
                    ),
                ),
            ],
        ),
    ]
