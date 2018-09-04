# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lending',
        'USER': 'business',
        'PASSWORD': 'qwer1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
