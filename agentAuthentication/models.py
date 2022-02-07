from tkinter import CASCADE
from django.conf import settings
from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings

class Agent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='agent', on_delete=models.CASCADE )
    agent_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    first_name = models.CharField(null=True, max_length=30, verbose_name= 'First Name')
    last_name = models.CharField(null=True, max_length=30, verbose_name= 'Last Name')
    country = CountryField()
    phone_number = models.CharField(max_length=14, null=True, unique=True, verbose_name='phone number', blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name

        