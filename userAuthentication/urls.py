from django import urls
from django.urls import path, include, re_path
# from .views import ApartmentApiView
from .views import CreateListAPIView, CreateUpdateDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import confirm_email

urlpatterns = [
    path('views/', CreateListAPIView.as_view()),
    path('views/<uuid:user_id>', CreateUpdateDestroyAPIView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
