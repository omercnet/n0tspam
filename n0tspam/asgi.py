"""
ASGI config for n0tspam project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import n0temail.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "n0tspam.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(n0temail.routing.websocket_urlpatterns)
        ),
    }
)
