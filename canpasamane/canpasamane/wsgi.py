"""
WSGI config for canpasamane project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
import signal
import time
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canpasamane.settings')



try:
    application = get_wsgi_application()
except Exception:
    if 'mod_wsgi' in sys.modules:
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
