from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_to_websocket(connection_id, message):
    channel_layer = get_channel_layer()
    print(channel_layer)
    async_to_sync(channel_layer.group_send)(
        f"connection_{connection_id}",
        {
            "type": "action",
            "message": message
        }
    )