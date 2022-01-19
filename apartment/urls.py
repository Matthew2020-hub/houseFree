from django import urls
from django.urls import path, include
# from .views import ApartmentApiView
from .views import CreateListAPIView, CreateUpdateDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('views/', CreateListAPIView.as_view()),
    path('views/<uuid:apartment_id>', CreateUpdateDestroyAPIView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
