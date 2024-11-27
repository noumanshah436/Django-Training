import os

# Import necessary components for ASGI and Channels routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

# Import WebSocket URL routing from the 'chat' app
from chat.routing import wsPattern

# Set the default settings module for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# Get the standard ASGI application for HTTP requests
http_response_app = get_asgi_application()

# Define the ASGI application with ProtocolTypeRouter
application = ProtocolTypeRouter({
    # Handle HTTP requests with the default Django ASGI application
    "http": http_response_app,
    # Handle WebSocket requests by routing them to wsPattern (websocket consumers)
    "websocket": URLRouter(wsPattern)
})



# This code sets up an ASGI application to handle both HTTP and WebSocket requests. 
# HTTP requests are handled by Django’s standard ASGI application, 
# while WebSocket requests are routed to wsPattern, which would be defined in chat app's routing file 
#   for handling real-time communication, like chat messages.
