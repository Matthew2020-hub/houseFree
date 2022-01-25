from tkinter import CASCADE
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
import uuid
# from .managers import CustomUserManager
# , AgentManager
# from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_superuser', True)

    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')

    #     return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class CustomUser(AbstractBaseUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    first_name = models.CharField(null=True, max_length=30, verbose_name= 'First Name')
    last_name = models.CharField(null=True, max_length=30, verbose_name= 'Last Name')
    home_address = models.CharField( max_length=30, null=True, verbose_name= 'Home Address', blank=False,)
    country = CountryField()
    phone_number = models.IntegerField(null=True, unique=True, verbose_name='phone number')
    date_created = models.DateTimeField()
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'home_address', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class Agent_info(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     user_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
#     first_name = models.CharField(blank=False, max_length=30, verbose_name= 'First Name')
#     last_name = models.CharField(blank=False, max_length=30, verbose_name= 'Last Name')
#     home_address = models.CharField( max_length=30, verbose_name= 'Home Address', blank=False,)
#     country = CountryField()
#     phone_number = models.IntegerField(blank=False, unique=True, verbose_name='phone number')
#     date_created = models.DateTimeField(verbose_name='date_created')
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'home_address', 'country', 'phone_number']

#     objects = AgentManager()

#     def __str__(self):
#         return self.email
