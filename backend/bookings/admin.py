from django.contrib import admin
from .models import (
    Temple, Devotee, DarshanSlot, DarshanBooking, 
    Pooja, PoojaBooking, Donation, Event, Volunteer
)

@admin.register(Temple)
class TempleAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'contact_phone')
    search_fields = ('name', 'city')

@admin.register(Devotee)
class DevoteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

@admin.register(DarshanSlot)
class DarshanSlotAdmin(admin.ModelAdmin):
    list_display = ('temple', 'date', 'start_time', 'end_time', 'max_capacity', 'booked_count')
    list_filter = ('temple', 'date')

@admin.register(DarshanBooking)
class DarshanBookingAdmin(admin.ModelAdmin):
    list_display = ('devotee', 'slot', 'created_at', 'status')
    list_filter = ('status', 'created_at')

@admin.register(Pooja)
class PoojaAdmin(admin.ModelAdmin):
    list_display = ('name', 'temple', 'price')
    list_filter = ('temple',)

@admin.register(PoojaBooking)
class PoojaBookingAdmin(admin.ModelAdmin):
    list_display = ('devotee', 'pooja', 'created_at', 'status')
    list_filter = ('status', 'created_at')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('devotee', 'amount', 'created_at', 'purpose')
    list_filter = ('created_at', 'purpose')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'temple', 'start_date', 'end_date')
    list_filter = ('temple', 'start_date')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('devotee', 'event', 'status')
    list_filter = ('status',)
