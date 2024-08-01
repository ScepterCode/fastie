from django.shortcuts import render
from django.db import models
from rest_framework import generics, permissions
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer

class ChatRoomListView(generics.ListCreateAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ChatRoom.objects.filter(models.Q(artisan=user) | models.Q(client=user))

class MessageListView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chat_room_id = self.kwargs['chat_room_id']
        return Message.objects.filter(chat_room_id=chat_room_id)

    def perform_create(self, serializer):
        chat_room_id = self.kwargs['chat_room_id']
        chat_room = ChatRoom.objects.get(id=chat_room_id)
        serializer.save(sender=self.request.user, chat_room=chat_room)
