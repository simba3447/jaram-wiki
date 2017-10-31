from jaram_wiki.settings.base import *
import dj_database_url

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'jaram_wiki',
#         'USER': 'admin',
#         'PASSWORD': 'Jaram@2017Admin',
#         'HOST': 'localhost',
#         'PORT': ''
#     }
# }
DATABASES['default'] =  dj_database_url.config()
