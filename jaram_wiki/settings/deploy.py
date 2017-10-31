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
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
