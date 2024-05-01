from .views import index, chat
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('chat/<str:username>', chat, name='chat')
]
