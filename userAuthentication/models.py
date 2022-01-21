from tkinter import CASCADE
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
import uuid
from .managers import CustomUserManager



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    first_name = models.CharField(blank=False, max_length=30, verbose_name= 'First Name')
    last_name = models.CharField(blank=False, max_length=30, verbose_name= 'Last Name')
    home_address = models.CharField( max_length=30, verbose_name= 'Home Address', blank=False,)
    country = CountryField()
    phone_number = models.IntegerField(blank=False, unique=True, verbose_name='phone number')
    date_created = models.DateTimeField(verbose_name='date_created')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'home_address', 'country', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

