from django.shortcuts import render

# Create your views here.
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from random import randint
import environ
# Initialise environment variables

@api_view(['GET', 'POST'])
def make_payment(name, email, amount, phone):
    env = environ.Env()
    environ.Env.read_env('transaction.env')
    serializer = PaymentSerializer
    auth_token = env('SECRET_KEY')
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
                "tx_ref":''+str(randint(111111,999999)),
                "amount":amount,
                "currency":"NGN",
                "redirect_url":"http://localhost:8000/callback",
                "payment_options":"card",
                "meta":{
                    "consumer_id":23,
                    "consumer_mac":"92a3-912ba-1192a"
                },
                "customer":{
                    "email":email,
                    "phonenumber":phone,
                    "name":name
                },
                "customizations":{
                    "title":"Supa houseFree",
                    "description":"a user-agent connct platform",
                    "logo":"https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
                }
                }
    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response_data = response.json()
    link=response_data['data']['link']
    return link