from cmath import phase
import email
from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(blank=False, max_length=30, verbose_name='name')
    email = models.EmailField(unique=True, verbose_name='email', blank=False)
    phone = models.CharField(max_length=12, unique=True, blank=False, verbose_name='phone number')
    date_created = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=20, blank=False)