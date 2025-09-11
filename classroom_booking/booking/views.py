from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'room1'},
    {'id': 2, 'name': 'room2'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'booking/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'booking/room.html', context)
