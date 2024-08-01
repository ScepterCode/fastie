
from django.urls import path
from .views import ChatRoomListView, MessageListView

urlpatterns = [
    path('rooms/', ChatRoomListView.as_view(), name='chat-rooms'),
    path('rooms/<int:chat_room_id>/messages/', MessageListView.as_view(), name='chat-messages'),
]