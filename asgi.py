"""
ASGI config for n0tspam project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from decouple import config
from django.core.asgi import get_asgi_application

config("DJANGO_SETTINGS_MODULE", default="settings")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import n0temail.routing


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(n0temail.routing.websocket_urlpatterns)
        ),
    }
)
