
from django.contrib import admin
from .models import ChatRoom, Message

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'artisan', 'client')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat_room', 'sender', 'content', 'timestamp')
    list_filter = ('chat_room', 'sender', 'timestamp')