import json
import logging

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.core.serializers.json import DjangoJSONEncoder

from .models import Email

class EmailConsumer(AsyncJsonWebsocketConsumer):

    email_name = None
    email_group_name = None
    logger = logging.getLogger(__name__)

    async def connect(self):
        self.email_name = self.scope["url_route"]["kwargs"]["email_name"]
        self.email_group_name = f"email_{self.email_name}"

        await self.channel_layer.group_add(
            self.email_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.email_group_name,
            self.channel_name,
        )

    async def receive_json(self, data: dict):
        data.update({"ack": True})
        await self.send_json(data)
        self.logger.debug(data)

    async def encode_json(self, data: dict):
        return json.dumps(data, cls=DjangoJSONEncoder)

    async def email_new(self, msg: dict):
        await self.send_json({"type": "new", "email": await self.get_email(msg['id'])})

    @database_sync_to_async
    def get_email(self, id: int):
        return list(Email.objects.filter(id=id).values())[0]
