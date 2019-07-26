"""
WSGI config for mosalam project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mosalam.settings.prod')
sys.path.append('/src/mosalam/settings')

application = get_wsgi_application()
