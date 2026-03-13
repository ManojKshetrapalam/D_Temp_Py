from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'temples', views.TempleViewSet)
router.register(r'devotees', views.DevoteeViewSet)
router.register(r'darshan-slots', views.DarshanSlotViewSet)
router.register(r'darshan-bookings', views.DarshanBookingViewSet)
router.register(r'poojas', views.PoojaViewSet)
router.register(r'pooja-bookings', views.PoojaBookingViewSet)
router.register(r'donations', views.DonationViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'volunteers', views.VolunteerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard-stats/', views.DashboardStatsView.as_view(), name='dashboard-stats'),
]
