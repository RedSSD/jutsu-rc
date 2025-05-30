from django.urls import re_path

from bot import consumers

websocket_urlpatterns = [
    re_path(r"ws/connection/(?P<token>[a-zA-Z0-9]+)/$", consumers.ControlConsumer.as_asgi()),
]