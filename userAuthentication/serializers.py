from dataclasses import fields
from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    model = CustomUser
    fields =  ['user_id', 'email', 'first_name', 'last_name', 'home_address', 'country', 'phone_number', 'Password']
