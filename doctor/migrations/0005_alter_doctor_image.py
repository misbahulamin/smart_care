# Generated by Django 5.0.7 on 2024-07-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0004_alter_review_doctor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="image",
            field=models.ImageField(upload_to="doctor/images/"),
        ),
    ]
