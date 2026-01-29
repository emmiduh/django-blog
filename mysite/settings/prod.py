from .base import *
from decouple import config

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "django-blog-h6pw.onrender.com"]
ADMINS = [
    ('Emmanuel I', 'emmiduh@gmail.com')
]
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : config('DB_NAME'),
        'USER' : config('DB_USER'),
        'PASSWORD' : config('DB_PASSWORD'),
        'HOST' : config('DB_HOST'),
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

