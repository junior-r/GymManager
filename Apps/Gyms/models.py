from django.db import models
from django_countries.fields import CountryField


class Gym(models.Model):
    legal_name = models.CharField(max_length=100, null=False, blank=False, unique=True, error_messages={
        'unique': 'Ya existe un Gimnasio con este nombre legal.'
    })
    trade_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    country = CountryField(blank=False, null=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey('Users.Manager', on_delete=models.CASCADE, related_name='user_gyms')

    def __str__(self):
        return self.legal_name


class Establishment(models.Model):
    legal_name = models.CharField(max_length=100, null=False, blank=False, unique=True, error_messages={
        'unique': 'Ya existe un Gimnasio con este nombre legal.'
    })
    trade_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    country = CountryField(blank=False, null=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='gym_establishments')
    user = models.ForeignKey('Users.CustomUser', limit_choices_to={'user_type': ['staff', 'manager']},
                             on_delete=models.CASCADE, related_name='user_gyms')

    def __str__(self):
        return self.legal_name
