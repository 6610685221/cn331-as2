from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Room(models.Model):
    room_id = models.CharField(max_length=10, primary_key=True, verbose_name='ID')
    room_name = models.CharField(max_length=200, verbose_name='Name')
    room_capacity = models.PositiveIntegerField(verbose_name='Capacity')
    room_hours = models.PositiveIntegerField(
        'Total Hours',
        validators=[MinValueValidator(0), MaxValueValidator(24)]
    )
    status = models.BooleanField(verbose_name='Status')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.room_name
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.room.room_name} booked by {self.user.username}"
