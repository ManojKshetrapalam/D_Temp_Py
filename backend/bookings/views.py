from rest_framework import viewsets
from .models import (
    Temple, Devotee, DarshanSlot, DarshanBooking, Pooja, PoojaBooking,
    Donation, Event, Volunteer
)
from .serializers import (
    TempleSerializer, DevoteeSerializer, DarshanSlotSerializer,
    DarshanBookingSerializer, PoojaSerializer, PoojaBookingSerializer,
    DonationSerializer, EventSerializer, VolunteerSerializer
)

class TempleViewSet(viewsets.ModelViewSet):
    queryset = Temple.objects.all()
    serializer_class = TempleSerializer

class DevoteeViewSet(viewsets.ModelViewSet):
    queryset = Devotee.objects.all()
    serializer_class = DevoteeSerializer

class DarshanSlotViewSet(viewsets.ModelViewSet):
    queryset = DarshanSlot.objects.all()
    serializer_class = DarshanSlotSerializer

class DarshanBookingViewSet(viewsets.ModelViewSet):
    queryset = DarshanBooking.objects.all()
    serializer_class = DarshanBookingSerializer

class PoojaViewSet(viewsets.ModelViewSet):
    queryset = Pooja.objects.all()
    serializer_class = PoojaSerializer

class PoojaBookingViewSet(viewsets.ModelViewSet):
    queryset = PoojaBooking.objects.all()
    serializer_class = PoojaBookingSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
