from channels.generic.websocket import AsyncWebsocketConsumer


class EmailConsumer(AsyncWebsocketConsumer):

    email_name = None
    email_group_name = None

    async def connect(self):
        self.email_name = self.scope["url_route"]["kwargs"]["email_name"].replace(
            "@", "._."
        )
        self.email_group_name = f"email_{self.email_name}"

        await self.channel_layer.group_add(self.email_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.email_group_name, self.channel_name)
