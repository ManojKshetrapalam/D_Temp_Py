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

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

class DashboardStatsView(APIView):
    def get(self, request):
        total_bookings = DarshanBooking.objects.count() + PoojaBooking.objects.count()
        active_temples = Temple.objects.count()
        total_donations = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        
        recent_bookings = DarshanBooking.objects.select_related('devotee', 'slot__temple').order_by('-created_at')[:5]
        bookings_data = []
        for b in recent_bookings:
            bookings_data.append({
                "devotee": b.devotee.name,
                "temple": b.slot.temple.name,
                "date_time": f"{b.slot.date} {b.slot.start_time}",
                "status": b.status
            })

        return Response({
            "total_bookings": f"{total_bookings:,}",
            "active_temples": active_temples,
            "total_donations": f"₹{total_donations:,.0f}",
            "recent_bookings": bookings_data
        })

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
