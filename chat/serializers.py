from rest_framework import serializers
from .models import ChatRoom, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']

class ChatRoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'artisan', 'client', 'messages']