"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()

try:
    from django.core.management import call_command
    from django.db import connection
    tables = connection.introspection.table_names()
    if 'core_profile' not in tables:
        print("Running one-time Vercel Neon initialization...")
        call_command('migrate', interactive=False)
        call_command('loaddata', 'datadump.json')
except Exception as e:
    print(f"Vercel auto-migrate failed: {e}")

app = application
