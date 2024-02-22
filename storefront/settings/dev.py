from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&n88zt%2a&0x@u_w5kaz0apyp44e)1&wt=h*h&7_7(0+cecx2-'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DJANGO_DEV_DATABASE_NAME'),
        'HOST': os.environ.get('DJANGO_DEV_DATABASE_HOST'),
        'USER': os.environ.get('DJANGO_DEV_DATABASE_USER'),
        'PASSWORD': os.environ.get('DJANGO_DEV_DATABASE_PASS'),
        'PORT': os.environ.get('DJANGO_DEV_DATABASE_PORT'),
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8001',
    'http://127.0.0.1:8001',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('DJANGO_DEV_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('DJANGO_DEV_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_DEV_EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('DJANGO_DEV_EMAIL_PORT')
DEFAULT_FROM_EMAIL = os.environ.get('DJANGO_DEV_FROM_EMAIL')
