"""
ASGI config for egaba project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import notification.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "egaba.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
})