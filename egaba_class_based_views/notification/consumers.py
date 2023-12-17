import django
django.setup()

import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from questions.models import Question
from accounts.models import UserProfile
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync, sync_to_async
import channels.layers

from channels.db import database_sync_to_async


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        user_profile = await sync_to_async(UserProfile.objects.get)(user=user)
        self.notif_room_name = f'notification-{user_profile.id}'

        await self.channel_layer.group_add(
            self.notif_room_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.notif_room_name,
            {
                "type": "send_notification",
                "text": message,
            },
        )

    async def send_notification(self, event):
        await self.send(text_data=json.dumps(event["text"]))
