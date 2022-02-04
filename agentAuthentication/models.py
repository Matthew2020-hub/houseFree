from django.db import models
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
import uuid
from django.contrib.auth.base_user import BaseUserManager
from dome.settings import AUTH_AGENT_MODEL


class CustomAgentManager(BaseUserManager):
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

class Agent(AbstractBaseUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    first_name = models.CharField(null=True, max_length=30, verbose_name= 'First Name')
    last_name = models.CharField(null=True, max_length=30, verbose_name= 'Last Name')
    home_address = models.CharField( max_length=30, null=True, verbose_name= 'Home Address', blank=False)
    country = CountryField()
    phone_number = models.CharField(max_length=14, null=True, unique=True, verbose_name='phone number', blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'home_address', 'phone_number']
    objects = CustomAgentManager()

    def __str__(self):
        return self.email




