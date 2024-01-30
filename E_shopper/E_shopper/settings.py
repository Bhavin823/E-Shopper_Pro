"""
Django settings for E_shopper project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hxv9tg85@0w825g#!(#_--g==i(vvi-dsy560qns$i^g#_$bm0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['e-shopper-pl0g.onrender.com']

# settings.py

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'e-shopper-pl0g.onrender.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'base_app',
    'category_app',
    'product_app',
    'user_app',
    'cart_app',
    'order_app',
    'payment_app',
    


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'E_shopper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'base_app', 'templates'),
        ],
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

WSGI_APPLICATION = 'E_shopper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME' : 'e-shopper',
#         'USER' : 'postgres',
#         'PASSWORD' : 'admin',
#         'HOST' : 'localhost',
#         'PORT' : '5432', 
#     }
# }

import dj_database_url
import os

os.environ["DATABASE_URL"] = "postgres://testdb_9vo5_user:Swa2dk9XN39TvAQTW8fhXGyjhw9XFdAW@dpg-cmr02r2cn0vc73dqiuo0-a.singapore-postgres.render.com/testdb_9vo5"
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"), conn_max_age=600)
}

# DATABASES = {
# 	"default": dj_database_url.parse(os.environ.get("postgres://testdb_9vo5_user:Swa2dk9XN39TvAQTW8fhXGyjhw9XFdAW@dpg-cmr02r2cn0vc73dqiuo0-a.singapore-postgres.render.com/testdb_9vo5"), engine='django.db.backends.postgresql')
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# STATIC_URL = 'static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
#     ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# as per render doc

STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = '/opt/render/project/src/E_shopper/staticfiles'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# as per redner doc

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# razorpay
RAZOR_KEY_ID = 'rzp_test_oIfjSKu51zvTk9'
RAZOR_KEY_SECRET = 'IBb3phnHZ3cASYkBD9GKFe4G'
