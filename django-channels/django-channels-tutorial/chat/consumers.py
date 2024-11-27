import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):

    # This method handles the WebSocket connection request
    async def connect(self):
        # Get room_name from the URL parameter
        room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = f"room_{room_name}"

        # Add the user to the group of the specified room
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        # Accept the WebSocket connection
        await self.accept()

    # This method handles disconnection requests
    async def disconnect(self, code):
        # Remove the user from the group of the specified room
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

        # Close the WebSocket connection
        self.close(code)

    # This method receives messages from the WebSocket
    async def receive(self, text_data):
        # Parse the received data (JSON format)
        data_json = json.loads(text_data)
        print("Received Data")
        print(data_json)

        # Prepare an event for the channel layer to send to other group members
        # The 'type' key is mandatory and tells Django Channels which method to call
        # 'send_message' will trigger the send_message method in this consumer
        event = {"type": "send_message", "message": data_json}

        # Send the message event to the group
        await self.channel_layer.group_send(self.room_name, event)

    # This method sends the message to WebSocket clients
    async def send_message(self, event):
        data = event["message"]

        # Save the message to the database asynchronously
        await self.create_message(data=data)

        # Prepare the response data to send to the WebSocket client
        response = {"sender": data["sender"], "message": data["message"]}

        # Send the message back to the WebSocket client
        await self.send(text_data=json.dumps({"message": response}))

    # This method is used to create a new message in the database
    @database_sync_to_async
    def create_message(self, data):
        # Get the room from the database using the room_name
        get_room = Room.objects.get(room_name=data["room_name"])

        # Check if the message already exists to avoid duplicates
        if not Message.objects.filter(
            message=data["message"], sender=data["sender"]
        ).exists():
            # Create a new message in the database
            new_message = Message.objects.create(
                room=get_room, message=data["message"], sender=data["sender"]
            )
