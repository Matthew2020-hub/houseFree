from unicodedata import name
from django import urls
from django.urls import path
# from .views import ApartmentApiView
from .import views

urlpatterns = [
    path('api/v1/contact-us', views.contact_us, name='contact us'),

]
