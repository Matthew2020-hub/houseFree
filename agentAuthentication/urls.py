from unicodedata import name
from django import urls
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import confirm_email
from  .views import (CreateListAPIView, Login, 
CreateUpdateDestroyAPIView,CreateUpdateAPIView, LogoutView, SetLoginView, CookiesLoginView)
from dome.settings import AUTHENTICATION_BACKENDS

urlpatterns = [
    path('rest-auth/agent-reg/', CreateListAPIView.as_view()),
    path('rest-auth/registration/<uuid:user_id>', CreateUpdateDestroyAPIView.as_view()),
    path('agent/login/', Login.as_view(), name='agent-login'),
    path('agent/', SetLoginView.as_view()),
    path('agent/logout/', LogoutView.as_view()),
    path('cookie/', CookiesLoginView.as_view()),
    path('tokens/', views.validate_authorization_code, name="code_validation"),
    path( 'agent-info/', views.google_get_agent_info, name="socialilogin"),
    path('rest-auth/logout/', views.logout, name="logout"),
    path('rest-auth/forget-password/<uuid:user_id>', CreateUpdateAPIView.as_view()),
    path('', include('rest_auth.urls')),
    path('agent-view/<uuid:user_id>', CreateUpdateDestroyAPIView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

