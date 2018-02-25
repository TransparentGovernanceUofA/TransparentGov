'''
Django settings to build on Travis CI
Taken and adapted from http://www.lesinskis.com/travis_ci_django.html
'''

import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.template.backends.django.DjangoTemplates',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
    }
}
