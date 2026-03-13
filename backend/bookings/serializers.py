from rest_framework import serializers
from .models import (
    Temple, Devotee, DarshanSlot, DarshanBooking, Pooja, PoojaBooking,
    Donation, Event, Volunteer
)

class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temple
        fields = '__all__'

class DevoteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devotee
        fields = '__all__'

class DarshanSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DarshanSlot
        fields = '__all__'

class DarshanBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DarshanBooking
        fields = '__all__'

class PoojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pooja
        fields = '__all__'

class PoojaBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoojaBooking
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
