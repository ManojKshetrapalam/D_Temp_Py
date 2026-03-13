from django.contrib import admin
from .models import (
    Temple, Devotee, DarshanSlot, DarshanBooking, 
    Pooja, PoojaBooking, Donation, Event, Volunteer
)

@admin.register(Temple)
class TempleAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_number')
    search_fields = ('name', 'location')

@admin.register(Devotee)
class DevoteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'phone_number')

@admin.register(DarshanSlot)
class DarshanSlotAdmin(admin.ModelAdmin):
    list_display = ('temple', 'date', 'start_time', 'end_time', 'capacity', 'booked_count')
    list_filter = ('temple', 'date')

@admin.register(DarshanBooking)
class DarshanBookingAdmin(admin.ModelAdmin):
    list_display = ('devotee', 'slot', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')

@admin.register(Pooja)
class PoojaAdmin(admin.ModelAdmin):
    list_display = ('name', 'temple', 'price')
    list_filter = ('temple',)

@admin.register(PoojaBooking)
class PoojaBookingAdmin(admin.ModelAdmin):
    list_display = ('devotee', 'pooja', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('devotee', 'amount', 'donation_date', 'purpose')
    list_filter = ('donation_date', 'purpose')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'temple', 'start_date', 'end_date')
    list_filter = ('temple', 'start_date')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('devotee', 'temple', 'role', 'status')
    list_filter = ('temple', 'status')
