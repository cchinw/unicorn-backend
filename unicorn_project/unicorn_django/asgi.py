"""
ASGI config for unicorn_django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import django
import dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    dotenv.read_dotenv(BASE_DIR, '.env')
except IsADirectoryError:
    dotenv.read_dotenv()

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unicorn_django.settings')

application = get_asgi_application()
