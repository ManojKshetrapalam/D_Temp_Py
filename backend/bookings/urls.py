from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TempleViewSet, DevoteeViewSet, DarshanSlotViewSet,
    DarshanBookingViewSet, PoojaViewSet, PoojaBookingViewSet,
    DonationViewSet, EventViewSet, VolunteerViewSet
)

router = DefaultRouter()
router.register(r'temples', TempleViewSet)
router.register(r'devotees', DevoteeViewSet)
router.register(r'darshan-slots', DarshanSlotViewSet)
router.register(r'darshan-bookings', DarshanBookingViewSet)
router.register(r'poojas', PoojaViewSet)
router.register(r'pooja-bookings', PoojaBookingViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'events', EventViewSet)
router.register(r'volunteers', VolunteerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
