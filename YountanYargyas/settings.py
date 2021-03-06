"""
Django settings for YountanYargyas project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from os import getenv, path
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = str(getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'main.apps.MainConfig',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'YountanYargyas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'YountanYargyas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_CODE = str(getenv('DATABASE_CODE'))

if DATABASE_CODE == "1":
    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.postgresql_psycopg2",
            'NAME': f"{str(getenv('DATABASE_NAME'))}",
            'USER': f"{str(getenv('DATABASE_USER'))}",
            'PASSWORD': f"{str(getenv('DATABASE_PASS'))}",
            'HOST': f"{str(getenv('DATABASE_HOST'))}",
            'PORT': f"{str(getenv('DATABASE_PORT'))}",
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.sqlite3",
            'NAME': BASE_DIR / "db.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# TinyMCE Configuration

TINYMCE_DEFAULT_CONFIG = {
    "height": "512px",
    "width": "100%",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks codesample code fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "fullscreen preview save print | undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | insertfile image media pageembed template link codesample anchor | a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,

    # Disable Relative URLs
    "relative_urls": False,
    "remove_script_host": True,
    "document_base_url": "/",

    # Custom codesample Languages
    # "codesample_languages": [{"text": "HTML/XML", "value": "markup"},
    #                          {"text": "JavaScript", "value": "javascript"},
    #                          {"text": "CSS", "value": "css"},
    #                          {"text": "PHP", "value": "php"},
    #                          {"text": "Ruby", "value": "ruby"},
    #                          {"text": "Python", "value": "python"},
    #                          {"text": "Java", "value": "java"},
    #                          {"text": "C", "value": "c"},
    #                          {"text": "C#", "value": "csharp"},
    #                          {"text": "C++", "value": "cpp"},],
}
# TINYMCE_SPELLCHECKER = True

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

# Media files

MEDIA_ROOT = path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
