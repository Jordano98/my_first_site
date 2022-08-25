
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

#Security Settings

X_FRAME_OPTIONS='SAMEORIGIN'
CSRF_COOKIE_SECURE = True #to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True #to avoid transmitting the session cookie over HTTP accidentally.
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 86400  # 1 day
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True