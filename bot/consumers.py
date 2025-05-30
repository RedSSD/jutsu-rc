import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ControlConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.token = self.scope['url_route']['kwargs']['token']
        self.connection_name = f"connection_{self.token}"

        await self.channel_layer.group_add(self.connection_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.connection_name, self.channel_name)

    async def receive(self, text_data):
        pass

    async def action(self, event):
        """Handles messages sent to the WebSocket group"""
        message = event["message"]["text"]  # Extract the message data
        await self.send(text_data=json.dumps({"action": message}))
