"""
WSGI config for transgov project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/

The Python script that acts as the Web Server Gateway Interface for the later deploy web app to production.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transgov.settings")

application = get_wsgi_application()
