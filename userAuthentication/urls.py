from unicodedata import name
from django import urls
from django.urls import path, include, re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import confirm_email
from  .views import (CreateListAPIView, Login, 
CreateUpdateDestroyAPIView,CreateUpdateAPIView, LogoutView, SetLoginView, CookiesLoginView)
from dome.settings import AUTHENTICATION_BACKENDS

urlpatterns = [
    path('rest-auth/registration/', CreateListAPIView.as_view()),
    path('user/login/', Login.as_view()),
    path('user/', SetLoginView.as_view()),
    path('user/logout/', LogoutView.as_view()),
    path('cookies/', CookiesLoginView.as_view()),
    path('token/', views.validate_authorization_code, name="code_validation"),
    path( 'user-info/', views.google_get_user_info, name="socialilogin"),
    path('rest-auth/logout/', views.logout, name="logout"),
    path('soc/', include('rest_framework_social_oauth2.urls')),
    path('rest-auth/forget_password/<uuid:user_id>', CreateUpdateAPIView.as_view()),
    path('rest-auth/registration/<uuid:user_id>', CreateUpdateDestroyAPIView.as_view()),
    path('', include('rest_auth.urls')),
    path('views/<uuid:user_id>', CreateUpdateDestroyAPIView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

