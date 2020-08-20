
from django.urls import path, include
from chat.views import chat

urlpatterns = [
    path('chat', chat, name='chat'),

]
