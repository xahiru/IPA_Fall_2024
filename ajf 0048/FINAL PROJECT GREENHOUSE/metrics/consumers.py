from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MetricsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'metrics'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'metrics_update',
                'message': message
            }
        )

    async def metrics_update(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))