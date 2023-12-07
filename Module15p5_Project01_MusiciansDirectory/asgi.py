"""
ASGI config for Module15p5_Project01_MusiciansDirectory project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Module15p5_Project01_MusiciansDirectory.settings')

application = get_asgi_application()
