import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ControlConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(json.dumps({"status": "connected"}))

    async def disconnect(self, close_code):
        print(f"Client disconnected: {close_code}")

    async def receive(self, text_data):
        pass
