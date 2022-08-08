
from my_first_site.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-593n1+(p_e&2bh_quzag(ncwz5%8$^)m3#t$9^c&ob%)%jinum'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['comphilia.com','www.comphilia.com']

#INSTALL_APPS=[]

#site framework
SITE_ID=3

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'comphili_travel',
        'USER': 'comphili_jordano',
        'PASSWORD': '09190860656ABc.',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_ROOT = BASE_DIR /'static'
MEDIA_ROOT = BASE_DIR /'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

#DEPLOY
#CSRF_COOKIE_SECURE=True