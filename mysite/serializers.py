from rest_framework.serializers import ModelSerializer
from .models import Booking

# Serializer for the booking of appointment
class BookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = ['name', 'phone_number', 'date', 'description', 'status', 'booking_id']
