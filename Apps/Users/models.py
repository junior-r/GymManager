import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from Apps.Gyms.models import Gym


def user_directory_image_path(instance, filename):
    image_name = 'Users/Images/Profile/{0}/{1}'.format(instance, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, image_name)
    if os.path.exists(full_path):
        os.remove(full_path)

    return image_name


identification_type_options = [
    ('Pasaporte', 'Pasaporte'),
    ('Cédula', 'Cédula')
]


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Cliente'),
        ('trainer', 'Entrenador'),
        ('manager', 'Gerente'),
        ('staff', 'Staff'),
    )
    GENDER_OPTIONS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    image = models.ImageField(upload_to=user_directory_image_path)
    address = models.CharField(max_length=200)
    country = CountryField(blank=False, null=False)
    identification_number = models.CharField(max_length=10, blank=False, null=False, unique=True)
    identification_type = models.CharField(choices=identification_type_options, max_length=11)
    phone = models.CharField(max_length=20)
    user_type = models.CharField(max_length=25, choices=USER_TYPE_CHOICES)
    gender = models.CharField(max_length=20, choices=GENDER_OPTIONS, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.get_username()


class Trainer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.get_username()


class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.get_username()


class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.get_username()


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, null=True, blank=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_username()


@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    Manager.objects.create(user=user)


user_signed_up.connect(create_profile)
