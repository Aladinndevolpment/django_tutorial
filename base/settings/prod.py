from .common import *

DEBUG = False
SECRET_KEY = 'django-insecure-1xac4#wkb_gm&i7bit4e4-5!!n+uo^jxf1)n3xup@rgxdbr8_p'
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
