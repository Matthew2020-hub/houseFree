from django import urls
from django.urls import path
# from .views import ApartmentApiView
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('views/', views.make_payment, name='make_payment'),
    # path('views/<uuid:apartment_id>', CreateUpdateDestroyAPIView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
