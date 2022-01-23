from dataclasses import fields
from django.forms import models
from .models import Payment
from rest_framework import serializers
class PaymentSerializer(serializers.ModelSerializer):
    model = Payment
    fields = ['name', 'email','phone', 'amount']