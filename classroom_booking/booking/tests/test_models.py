from django.test import TestCase
from django.contrib.auth.models import User
from booking.models import Room, Booking

class RoomModelTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(
            room_id='R101',
            room_name='Lecture Hall 1',
            room_capacity=50,
            room_hours=8,
            status=True,
            description='Main lecture hall'
        )

    def test_room_creation(self):
        self.assertEqual(self.room.room_name, 'Lecture Hall 1')
        self.assertTrue(self.room.status)
        self.assertLessEqual(self.room.room_hours, 24)
        self.assertGreaterEqual(self.room.room_hours, 0)

    def test_room_str_method(self):
        self.assertEqual(str(self.room), 'Lecture Hall 1')


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', password='testpass123')
        self.room = Room.objects.create(
            room_id='R102',
            room_name='Computer Lab',
            room_capacity=30,
            room_hours=6,
            status=True
        )
        self.booking = Booking.objects.create(room=self.room, user=self.user)

    def test_booking_creation(self):
        self.assertEqual(self.booking.room.room_name, 'Computer Lab')
        self.assertEqual(self.booking.user.username, 'john')

    def test_booking_str_method(self):
        expected_str = "Computer Lab booked by john"
        self.assertEqual(str(self.booking), expected_str)
