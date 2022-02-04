from dataclasses import fields
from django.forms import CharField, models
from django.shortcuts import redirect
from .models import Agent
import requests
from rest_framework import serializers

from rest_auth.serializers import PasswordResetSerializer

class AgentSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Agent
        fields =  ['user_id', 'email', 'first_name', 'last_name', 'home_address',
          'country', 'phone_number', 'password', 'password2']
        extra_kwargs = {
            'password2': {
                'write_only':True
            }
        }
    def save(self):
        user = Agent(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['first_name'],
            home_address=self.validated_data['home_address'],
            country=self.validated_data['country'],
            phone_number=self.validated_data['phone_number'],
            password = self.validated_data['password'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user



class AgentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def __str__(self):
        return self.email

class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField()

class CustomPasswordResetSerializer(PasswordResetSerializer):
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)

class GetAcessTokenSerializer(serializers.Serializer):
    code = serializers.CharField()
   
