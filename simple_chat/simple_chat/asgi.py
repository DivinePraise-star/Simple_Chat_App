"""
ASGI config for simple_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import simple_chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_chat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            simple_chat.routing.websocket_urlpatterns
        )
    ),
})
