# Generated by Django 4.2.6 on 2023-12-27 10:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_user_is_active_user_is_admin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="otp",
            name="Full_name",
        ),
        migrations.RemoveField(
            model_name="otp",
            name="email",
        ),
        migrations.RemoveField(
            model_name="otp",
            name="image",
        ),
        migrations.RemoveField(
            model_name="otp",
            name="is_doctor",
        ),
        migrations.RemoveField(
            model_name="otp",
            name="is_patient",
        ),
        migrations.RemoveField(
            model_name="otp",
            name="username",
        ),
    ]
