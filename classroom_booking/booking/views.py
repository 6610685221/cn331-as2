from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'booking/home.html', context)

def room(request, pk):
    room = Room.objects.get(room_id=pk)
    context = {'room': room}
    return render(request, 'booking/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'booking/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(room_id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'booking/room_form.html',context)

def deleteRoom(request, pk):
    room = Room.objects.get(room_id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'booking/delete.html', {'obj': room})