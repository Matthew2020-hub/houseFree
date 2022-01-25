from django import urls
from django.urls import path, include, re_path
# from .views import ApartmentApiView
from .views import CreateUpdateDestroyAPIView, ListTodo
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import confirm_email
from .import views

urlpatterns = [
    path('views/', ListTodo.as_view()),
    path('', include('rest_auth.urls')),
    path('views/<uuid:user_id>', CreateUpdateDestroyAPIView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
