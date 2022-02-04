from django import urls
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('view/', views.make_payment, name='make_payment'),
    path('verify/', views.verify_transaction, name='verify_payment'),
    path('withdraw/', views.agent_withdrawal, name='verify_payment'),
    path('balance/', views.dashboard, name='balance'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
