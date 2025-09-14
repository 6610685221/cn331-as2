from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('',views.home, name='home' ),
    path('room/<str:pk>/', views.room, name='room'),
    path('room/room-booking/<str:pk>/',views.room_booking, name='room-booking'),
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/cancel-booking/<str:pk>/', views.cancelBooking, name='cancel-booking'),

    path('create-room/',views.createRoom, name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom, name='delete-room'),
]