from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from booking.models import Room, Booking

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(username='john', password='pass1234')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass')

        self.room = Room.objects.create(
            room_id='R001',
            room_name='Room 101',
            room_capacity=20,
            room_hours=5,
            status=True
        )

    def test_login_view_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'john',
            'password': 'pass1234'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to home

    def test_logout_view(self):
        self.client.login(username='john', password='pass1234')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect to home

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after register

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Room 101')

    def test_room_detail_view(self):
        response = self.client.get(reverse('room', args=[self.room.room_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Room 101')

    def test_booking_room_success(self):
        self.client.login(username='john', password='pass1234')
        response = self.client.post(reverse('room-booking', args=[self.room.room_id]))
        self.assertRedirects(response, reverse('home'))
        self.room.refresh_from_db()
        self.assertEqual(self.room.room_hours, 4)
        self.assertTrue(Booking.objects.filter(user=self.user, room=self.room).exists())

    def test_cancel_booking(self):
        Booking.objects.create(user=self.user, room=self.room)
        self.room.room_hours = 4
        self.room.save()
        self.client.login(username='john', password='pass1234')
        response = self.client.post(reverse('cancel-booking', args=[self.room.room_id]))
        self.assertRedirects(response, reverse('schedule'))
        self.assertFalse(Booking.objects.filter(user=self.user, room=self.room).exists())
        self.room.refresh_from_db()
        self.assertEqual(self.room.room_hours, 5)

    def test_create_room_admin_only(self):
        self.client.login(username='john', password='pass1234')  # Not admin
        response = self.client.get(reverse('create-room'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're not allow to be here.")

        self.client.logout()
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('create-room'))
        self.assertEqual(response.status_code, 200)
