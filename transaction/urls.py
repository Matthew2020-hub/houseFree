from django import urls
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('callback/', views.make_payment, name='make_payment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
