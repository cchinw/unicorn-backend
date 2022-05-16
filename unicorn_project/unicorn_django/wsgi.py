"""
WSGI config for unicorn_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    dotenv.read_dotenv(BASE_DIR, '.env')
except IsADirectoryError:
    dotenv.read_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unicorn_django.settings')

application = get_wsgi_application()
