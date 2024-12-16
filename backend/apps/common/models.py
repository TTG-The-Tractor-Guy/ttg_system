from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class TTGUserManager(BaseUserManager):
    def create_user(self, phone_number, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and phone_number.
        """
        if not phone_number:
            raise ValueError(_('The Phone number must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and phone_number.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, email, password, **extra_fields)


class TTGUser(AbstractUser):
    # Remove the username field since we will use the phone number instead
    username = None  # Remove the default username field
    phone_number = models.CharField(max_length=15, unique=True)  # Use phone_number as the unique identifier
    email = models.EmailField(unique=True)  # Email must also be unique

    USERNAME_FIELD = 'phone_number'  # Use phone_number as the login field
    REQUIRED_FIELDS = ['email']  # Email will be required for creating a user

    objects = TTGUserManager()
    def __str__(self):
        return self.phone_number  # Use phone_number as the string representation



