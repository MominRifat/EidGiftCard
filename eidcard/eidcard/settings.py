import os
from pathlib import Path
import os
import dj_database_url


# --------------------------
# BASE DIRECTORIES
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent  #  root folder
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  #  static files

# --------------------------
# SECURITY
# --------------------------
SECRET_KEY = SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-dev-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'  # set False in production
ALLOWED_HOSTS = ['*']  # allows all  domains

# --------------------------
# APPLICATIONS
# --------------------------
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'card',
]

# --------------------------
# MIDDLEWARE
# --------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serves static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------
# URL & WSGI
# --------------------------
ROOT_URLCONF = 'eidcard.urls'
WSGI_APPLICATION = 'eidcard.wsgi.application'

# --------------------------
# TEMPLATES
# --------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # main templates folder
        'APP_DIRS': True,  # look for templates inside apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --------------------------
# DATABASE
# --------------------------
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# --------------------------
# PASSWORD VALIDATORS
# --------------------------
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

# --------------------------
# INTERNATIONALIZATION
# --------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------
# STATIC FILES (CSS, JS, Images)
# --------------------------
STATIC_URL = '/static/'  # URL prefix
STATICFILES_DIRS = [STATIC_DIR]  # development folder
STATIC_ROOT = STATIC_ROOT  # production folder (collectstatic will copy files here)

# --------------------------
# WHITENOISE CONFIG (optional extra for caching)
# --------------------------
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'