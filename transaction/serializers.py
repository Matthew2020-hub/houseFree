from dataclasses import fields
import email
from email.policy import default
from django.forms import models
from .models import Payment
import uuid
from rest_framework import serializers


# class WalletSerializer(serializers.ModelSerializer):
#     class Meta:
#         models = 
#         fields = "__all__"
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def __str__(self):
        return self.amount

class WithdrawalSerializer(serializers.Serializer):
    account_number = serializers.CharField()
    account_bank = serializers.CharField(max_length=3)
    amount = serializers.CharField()
    narration = serializers.CharField()
    currency = serializers.CharField(max_length=3)
    reference = serializers.UUIDField(default=uuid.uuid4)
    email = serializers.EmailField
    debit_currency = serializers.CharField(default='NGN')
    account_id = serializers.CharField()
    withdrawal_date = serializers.DateTimeField()