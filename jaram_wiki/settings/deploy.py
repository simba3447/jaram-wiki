from jaram_wiki.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jaram_wiki',
        'USER': 'admin',
        'PASSWORD': 'Jaram@2017Admin',
        'HOST': 'localhost',
        'PORT': ''
    }
}
