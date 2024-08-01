
from django.db import models
from accounts.models import User

class ChatRoom(models.Model):
    artisan = models.ForeignKey(User, related_name='artisan_chats', on_delete=models.CASCADE)
    client = models.ForeignKey(User, related_name='client_chats', on_delete=models.CASCADE)

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
