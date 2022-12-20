from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

from phonenumber_field.modelfields import PhoneNumberField


class NewUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        """Ensure email are in the lower case"""
        self.email = self.email.lower()
        self.username = self.username.lower()
        super(NewUser, self).save(*args, **kwargs)
