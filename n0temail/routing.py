# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/email/(?P<email_name>\S+)/$", consumers.EmailConsumer.as_asgi()),
]
