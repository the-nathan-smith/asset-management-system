from sys import flags
from telnetlib import STATUS
from django.db import models

class Laptop(models.Model):
    type_choices = (
        ('SURFACEPRO', 'Surface Pro'),
        ('MACBOOK', 'MacBook'),
        ('THINKPAD', 'Thinkpad')
    )
    type = models.CharField(max_length=100, choices=type_choices, blank=False)

    owner = models.CharField(max_length=100, blank=False) #This needs changing to a User

    status_choices = (
        ('AVAILABLE', 'Device is available to be assigned'),
        ('ASSIGNED', 'Device is assigned to a staff member'),
        ('SETUP_REQUIRED', 'This device needs setting up before it can be assigned'),
    )
    status =models.CharField(max_length=100, choices=status_choices, blank=False)


    def __str__(self):
        return 'Type: {0} | Owner: {1} | Status: {2}'.format(self.type, self.owner, self.status)


class Mobile(models.Model):
    type_choices = (
        ('ANDROID', 'Android'),
        ('IPHONE', 'iPhone'),
        ('SAMSUNG', 'Samsung')
    )
    type = models.CharField(max_length=100, choices=type_choices, blank=False)

    owner = models.CharField(max_length=100, blank=False) #This needs changing to a User

    status_choices = (
        ('AVAILABLE', 'Device is available to be assigned'),
        ('ASSIGNED', 'Device is assigned to a staff member'),
        ('SETUP_REQUIRED', 'This device needs setting up before it can be assigned'),
    )
    status =models.CharField(max_length=100, choices=status_choices, blank=False)


    def __str__(self):
        return 'Type: {0} | Owner: {1} | Status: {2}'.format(self.type, self.owner, self.status)