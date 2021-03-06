"""
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
See deployment tips:
https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
"""

import os
import dj_database_url

if 'DEVELOPMENT' in os.environ:
    if os.environ.get('DEVELOPMENT') == 'true' or 1:
        development = 1
    else:
        development = 0
else:
    development = 0

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on  in production!
DEBUG = development
ALLOWED_HOSTS = [os.environ.get('HOSTNAME')]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'whitenoise.runserver_nostatic',
    'storages',
    'django_forms_bootstrap',
    'crispy_forms',
    'Home',
    'bugs',
    'cart',
    'checkout',
    'charts',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'django_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.context.cart_contents',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_app.wsgi.application'


# If You are developing locally use db.sqlite, on server use server db
# Note: your local system should have env variable DEVELOPMENT=1

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    print('Database URL not found. Using SQLite instead')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# FOR AMAZON S3
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=999999999'
}

# For testing purpose, you can check if mail is actually sending
# to the console using that line:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# GET ENVIRONMENTAL VARIABLES
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME =  os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = str(AWS_STORAGE_BUCKET_NAME) + '.s3.amazonaws.com'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Use AMAZON S3 only on remote server
# And on localhost use local staticfiles
if not development:
    STATICFILES_LOCATION = 'staticfiles'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    host_images_link = 'https://' + AWS_S3_CUSTOM_DOMAIN + str(MEDIA_URL)
else:
    STATICFILES_LOCATION = 'staticfiles'
    STATIC_URL = '/staticfiles/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'staticfiles'),
    ]
    host_images_link = 'http://' + os.environ.get('HOSTNAME') + ':' + os.environ.get('PORT') + str(MEDIA_URL)


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'Home.backends.EmailAuth',
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
