from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("PROD_SECRET_KEY")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("PROD_DB_NAME"),
        'USER': os.environ.get("PROD_DB_USER"),
        'PASSWORD': os.environ.get("PROD_DB_PASSWORD"),
        'HOST': os.environ.get("PROD_DB_HOST"),
        'PORT': os.environ.get("PROD_DB_PORT", 5432)
    }
}

