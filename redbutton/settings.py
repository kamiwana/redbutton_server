"""
Django settings for redbutton project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.config_secret')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config_secret['production']['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

import requests

def get_ec2_instance_ip():
    """
    Tries to obtain the IP address of the current EC2 instance in AWS
    """
    try:
        ip = requests.get(
          'http://169.254.169.254/latest/meta-data/local-ipv4',
          timeout=0.01
        ).text
    except requests.exceptions.ConnectionError:
        return None
    return ip


AWS_LOCAL_IP = get_ec2_instance_ip()
ALLOWED_HOSTS = [AWS_LOCAL_IP, 'www.redbutton-aws.ml', 'etc', '.amazonaws.com','localhost', '127.0.0.1','www.redbuttonserver.com']

LOGIN_REDIRECT_URL = '/member/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = config_secret['email']['host_user']
EMAIL_HOST_PASSWORD = config_secret['email']['host_password']

EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
AWS_HOST = config_secret['aws']['aws_host']
AWS_ACCESS_KEY_ID = config_secret['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret['aws']['s3_bucket_name']
AWS_S3_CUSTOM_DOMAIN = 'dc9bc8v76fw69.cloudfront.net'
#AWS_S3_CUSTOM_DOMAIN = '%s/%s' % (AWS_HOST, AWS_STORAGE_BUCKET_NAME)
DEFAULT_FILE_STORAGE = 'redbutton.storage_backends.MediaStorage'

AWS_S3_OBJECT_PARAMETERS = {
     'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

#STATIC_URL='https://%s/%s/'%(AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)
STATIC_URL = 'https://dc9bc8v76fw69.cloudfront.net/'
MEDIA_URL = 'https://dc9bc8v76fw69.cloudfront.net/'

STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'redbutton',  # DB명
            'USER': 'root',  # 데이터베이스계정
            'PASSWORD': '',  # 계정비밀번호
            'HOST': '127.0.0.1',  # 데이테베이스주소(IP)
            'OPTIONS': {
                "init_command": "SET GLOBAL max_connections = 100000",
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config_secret['db']['name'],
            'USER': config_secret['db']['user'],
            'PASSWORD': config_secret['db']['password'],
            'HOST': config_secret['db']['host'],
            'PORT': '3306',
            'OPTIONS': {
                   "init_command": "SET GLOBAL max_connections = 100000",
            }
        }
    }

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'rest_framework_swagger',
    'django.contrib.staticfiles',
 #   'django_extensions',
    'gameinfo',
    'branch',
    'branch_gameinfo',
    'api',
    'member',
    'main',
    'etc',
    'togeter',
    'game_thema',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'request_logging.middleware.LoggingMiddleware',
]

ROOT_URLCONF = 'redbutton.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


DATA_UPLOAD_MAX_MEMORY_SIZE = 1000000000

LOG_FILE = os.path.join(os.path.dirname(__file__), '..', 'redbuttonlog.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'propagate': False,
            'level': 'ERROR',
        },
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'redbutton': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
