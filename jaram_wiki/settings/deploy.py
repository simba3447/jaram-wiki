from jaram_wiki.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jaram_wiki',
        'USER': 'admin',
        'PASSWORD': SECRET_KEY,
        'HOST': 'localhost',
        'PORT': ''
    }
}
