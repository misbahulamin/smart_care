# Generated by Django 5.0.7 on 2024-07-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0002_alter_appointment_appointment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="appointment_status",
            field=models.IntegerField(
                choices=[("1", "Completed"), ("2", "Pending"), ("3", "Runing")],
                default="Pending",
            ),
        ),
    ]
