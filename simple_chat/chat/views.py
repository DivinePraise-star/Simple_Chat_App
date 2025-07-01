from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Message, ChatRoom

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')

def room(request, room_name):
    room, _ = ChatRoom.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')[:50]
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages
    })

@login_required
def profile(request):
    return redirect('room', room_name='lobby')
