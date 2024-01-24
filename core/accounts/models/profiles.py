from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User
from django.db import models

from ..validations.profile import validate_profile_title, validate_profile_email


# patient profile start.
class BloodType(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class ProfilePatient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=1000, validators=[validate_profile_title])
    image = models.ImageField(upload_to='images/profile/patient', blank=True, null=True)
    email = models.EmailField(max_length=1000, validators=[validate_profile_email], unique=True)
    status = models.BooleanField(default=True)
    bio = models.TextField(max_length=100000, blank=True, null=True)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE, blank=True, null=True)
    heart_beat = models.SmallIntegerField(blank=True, null=True)
    body_water = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hemoglobin = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'username:{self.user}-id:{self.user.id}'


@receiver(post_save, sender=User)
def create_patient_profile(sender, created, instance, **kwargs):
    if created:
        if instance.user.is_patient:
            ProfilePatient.objects.create(
                user=instance,
                username=instance.user.username,
                email=instance.user.email,

            )


# patient profile end.

# doctor profile start.

class Expertise(models.Model):
    name = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.name


class ProfileDoctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, validators=[validate_profile_title])
    email = models.EmailField(validators=[validate_profile_email], unique=True)
    bio = models.TextField(max_length=1000000, blank=True, null=True)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    patients = models.IntegerField()
    reserve = models.IntegerField()
    canceled = models.IntegerField()
    instantaneous = models.IntegerField()

    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def create_doctor_profile(sender, created, instance, **kwargs):
    if created:
        if instance.user.is_doctor:
            ProfileDoctor.objects.create(
                user=instance,
                username=instance.user.username,
                email=instance.user.email
            )
