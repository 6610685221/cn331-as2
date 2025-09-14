from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Booking
from .forms import RoomForm

# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect.')

    context = {'page': page}
    return render(request, 'booking/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'booking/login_register.html',{'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(room_name__icontains=q) |
        Q(room_id__icontains=q)
    )
    room_count = rooms.count()
    context = {'rooms': rooms, 'room_count': room_count}
    return render(request, 'booking/home.html', context)

def room(request, pk):
    room = Room.objects.get(room_id=pk)
    bookings = room.bookings.select_related('user')
    context = {'room': room, 'bookings': bookings}
    return render(request, 'booking/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if not request.user.is_superuser:
        return HttpResponse('You\'re not allow to be here.')

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'booking/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(room_id=pk)
    form = RoomForm(instance=room)

    if not request.user.is_superuser:
        return HttpResponse('You\'re not allow to be here.')


    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'booking/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(pk=pk)

    if not request.user.is_superuser:
        return HttpResponse('You\'re not allow to be here.')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'booking/delete.html', {'obj': room})


@login_required(login_url='login')
def room_booking(request, pk):
    room = Room.objects.get(room_id=pk)
    user = request.user

    if room.room_hours <= 0 or not room.status:
        messages.error(request, 'This room is not available for booking.')
        return redirect('room', pk=pk)
    
    if Booking.objects.filter(user=user, room=room).exists():
        messages.error(request, 'You have already booked this room.')
        return redirect('room', pk=pk)

    if request.method == 'POST':
        Booking.objects.create(user=user, room=room)
        room.room_hours -= 1

        if room.room_hours == 0:
            room.status = False
        
        room.save()
        messages.success(request, 'Room booked successfully.')
        return redirect('home')
        

    context = {'room': room}
    return render(request, 'booking/room_booking.html', context)

@login_required(login_url='login')
def schedule(request):
    bookings = Booking.objects.filter(user=request.user).select_related('room', 'user')
    context = {'bookings': bookings}
    return render(request, 'booking/schedule.html', context)

def cancelBooking(request, pk):
    booking = Booking.objects.get(room__room_id=pk, user=request.user)
    room = booking.room

    if request.method == 'POST':
        room.room_hours += 1
        room.status = True
        room.save()
        booking.delete()
        messages.success(request, 'Booking cancelled successfully.')
        return redirect('schedule')

    context = {'booking': booking}
    return render(request, 'booking/cancel_booking.html', context)

