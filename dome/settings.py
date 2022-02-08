"""
Django settings for dome project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from distutils.debug import DEBUG
from pathlib import Path

import os
from pickle import TRUE
from tkinter.tix import Tree
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.shortcuts import redirect
import environ
from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_ROOT = BASE_DIR / 'staticfiles'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dome.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

env = environ.Env()
# reading .env file
environ.Env.read_env('freeHouse.env')
DEBUG = True
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")
FLUTTERWAVE_KEY=env("FLUTTERWAVE_KEY")
cloudinary.config( 
  cloud_name=env("CLOUD_NAME"), 
  api_key=env("API_KEY"), 
  api_secret=env("API_SECRET"),
  secure = True
)
SECRET_KEY = os.environ.get('DJANGO_KEY')
CLOUDINARY_URL="cloudinary://313926842933816:DSBYok2TOrxqZjMKrEp8nNM_OcA@housefree"
# DEBUG=True
# Facebook configuration

SOCIAL_AUTH_GOOGLE_KEY = env('GOOGLE_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_SECRET = env('GOOGLE_CLIENT_KEY')
redirect_uri = env('redirect_uri')
project_id = env('project_id')

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook. Email is not sent by default, to get it, you must request the email permission:
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_PIPELINE = (
'social_core.pipeline.social_auth.social_details',
'social_core.pipeline.social_auth.social_uid',
'social_core.pipeline.social_auth.auth_allowed',
'social_core.pipeline.social_auth.social_user',
'social_core.pipeline.user.get_username',
'social_core.pipeline.social_auth.associate_by_email',
'social_core.pipeline.user.create_user',
'social_core.pipeline.social_auth.associate_user',
'social_core.pipeline.social_auth.load_extra_data',
'social_core.pipeline.user.user_details', )

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',  
    ),
    'DEFAULT_PERMISSIONS_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-0srq8vs)x)=#z5)wpj3h*mnwn&1%zk&#bci^_ftv#0io#sv5t7'

# SECURITY WARNING: don't run with debug turned on in production!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': env("DATABASE_HOST"),
        'PORT': env("DATABASE_PORT"),
    }
}
ALLOWED_HOSTS = ['localhost','127.0.0.1','house-free.herokuapp.com']
# ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'whitenoise.runserver_nostatic'
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'cloudinary',
    'cloudinary_storage',
    'apartment',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'rest_auth',
    'allauth',
    'social_django',
    'oauth2_provider',
    'django_countries',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'corsheaders',
    'userAuthentication',
    'transaction',
    'agentAuthentication',
    'message',
]

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'userAuthentication.serializers.CustomUserSerializer',
    'AGENT_DETAILS_SERIALIZER': 'agentAuthentication.serializers.AgentSerializer',
    'LOGIN_SERIALIZER': 'userAuthentication.serializers.LoginUserSerializer',
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'dome.urls'

AUTH_USER_MODEL = 'userAuthentication.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dome.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'housefree189@gmail.com'
EMAIL_HOST_PASSWORD = 'respect1242'
EMAIL_USE_TLS = True
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# CorsHeaders configuration
CORS_ORIGIN_ALLOW_ALL =True
CORS_ALLOW_CREDENTIALS =True
from django.urls import reverse_lazy
LOGIN_URL = reverse_lazy('agent-login')
