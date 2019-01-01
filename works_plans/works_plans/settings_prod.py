DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'workPlansDB',
        'USER' : 'django_plans',
        'PASSWORD' : 'test123',
        'HOST' : '127.0.0.1',
        'PORT' : '',
    }
}
