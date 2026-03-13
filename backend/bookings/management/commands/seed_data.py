from django.core.management.base import BaseCommand
from bookings.models import Temple, DarshanSlot, Pooja, Event, Devotee
from datetime import date, time, timedelta, datetime
import random

class Command(BaseCommand):
    help = 'Seeds the database with initial temple data starting from today'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # 1. Create a Temple
        temple, created = Temple.objects.get_or_create(
            name="Durgadevi Temple",
            defaults={
                "address": "Main Temple Road",
                "city": "Mumbai",
                "state": "Maharashtra",
                "country": "India",
                "opening_time": time(6, 0),
                "closing_time": time(21, 0),
                "contact_phone": "+91 9876543210"
            }
        )
        if created:
            self.stdout.write(f'Created Temple: {temple.name}')
        else:
            self.stdout.write(f'Using existing Temple: {temple.name}')

        # 2. Generate Darshan Slots for next 30 days
        start_date = date.today()
        slots_created = 0
        for i in range(30):
            current_date = start_date + timedelta(days=i)
            # Create morning and evening slots
            time_slots = [
                (time(7, 0), time(9, 0)),
                (time(10, 0), time(12, 0)),
                (time(17, 0), time(19, 0)),
                (time(19, 30), time(21, 0))
            ]
            
            for start_t, end_t in time_slots:
                slot, created = DarshanSlot.objects.get_or_create(
                    temple=temple,
                    date=current_date,
                    start_time=start_t,
                    end_time=end_t,
                    defaults={
                        "max_capacity": 50,
                        "booked_count": 0,
                        "status": "open"
                    }
                )
                if created:
                    slots_created += 1

        self.stdout.write(f'Created {slots_created} Darshan slots.')

        # 3. Create sample Poojas
        poojas = [
            {"name": "Morning Aarti", "price": 501.00},
            {"name": "Special Archana", "price": 251.00},
            {"name": "Vahana Pooja", "price": 1001.00},
            {"name": "Satyanarayan Vrat", "price": 2501.00}
        ]
        for p_data in poojas:
            pooja, created = Pooja.objects.get_or_create(
                temple=temple,
                name=p_data["name"],
                defaults={"price": p_data["price"], "description": f"Daily {p_data['name']} service"}
            )
            if created:
                self.stdout.write(f'Created Pooja: {pooja.name}')

        # 4. Create sample Events
        events = [
            {"title": "Maha Shivaratri Celebration", "days_away": 10},
            {"title": "Navratri Festival", "days_away": 25},
            {"title": "Weekly Bhajan Sandhya", "days_away": 2}
        ]
        for e_data in events:
            e_start = datetime.combine(date.today() + timedelta(days=e_data["days_away"]), time(18, 0))
            e_end = e_start + timedelta(hours=3)
            event, created = Event.objects.get_or_create(
                temple=temple,
                title=e_data["title"],
                defaults={
                    "description": f"Grand celebration of {e_data['title']}",
                    "start_date": e_start,
                    "end_date": e_end,
                    "location": "Temple Main Hall"
                }
            )
            if created:
                self.stdout.write(f'Created Event: {event.title}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded data.'))
