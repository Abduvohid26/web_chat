from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ChatGroup
from .models import ChatGroup
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def index(request):
    users = User.objects.exclude(id=request.user.id)
    context = {'users': users}
    return render(request, 'index.html', context)


@login_required()
def chat(request, username):
    users = User.objects.exclude(id=request.user.id)
    user1 = request.user
    user2 = User.objects.get(username=username)
    chat_group = ChatGroup.objects.filter(users=user1).filter(users=user2).first()
    if not chat_group:
        chat_group = ChatGroup.objects.create(name=f'chat_between__{user1.username}__and__{user2.username}')
        chat_group.users.add(user1, user2)

    context = {'users': users, 'user': user2, 'chat_group': chat_group}
    return render(request, 'chat.html', context)
