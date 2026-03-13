from django.db import models

class Temple(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        db_table = 'temples'

    def __str__(self):
        return self.name

class Devotee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'devotees'

    def __str__(self):
        return self.name

class DarshanSlot(models.Model):
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE, related_name='darshan_slots')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_capacity = models.IntegerField()
    booked_count = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed'), ('full', 'Full')], default='open')

    class Meta:
        db_table = 'darshan_slots'

    def __str__(self):
        return f"{self.temple.name} - {self.date} ({self.start_time}-{self.end_time})"

class DarshanBooking(models.Model):
    slot = models.ForeignKey(DarshanSlot, on_delete=models.CASCADE, related_name='bookings')
    devotee = models.ForeignKey(Devotee, on_delete=models.CASCADE, related_name='darshan_bookings')
    booking_reference = models.CharField(max_length=100, unique=True)
    num_people = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'darshan_bookings'

    def __str__(self):
        return f"Booking {self.booking_reference} - {self.devotee.name}"

class Pooja(models.Model):
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE, related_name='poojas')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} at {self.temple.name}"

class PoojaBooking(models.Model):
    pooja = models.ForeignKey(Pooja, on_delete=models.CASCADE, related_name='bookings')
    devotee = models.ForeignKey(Devotee, on_delete=models.CASCADE, related_name='pooja_bookings')
    date = models.DateField()
    booking_reference = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pooja {self.pooja.name} - {self.devotee.name}"

class Donation(models.Model):
    devotee = models.ForeignKey(Devotee, on_delete=models.CASCADE, related_name='donations')
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, default='success')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation {self.transaction_id} - {self.devotee.name}"

class Event(models.Model):
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class Volunteer(models.Model):
    devotee = models.ForeignKey(Devotee, on_delete=models.CASCADE, related_name='volunteering')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, related_name='volunteers')
    skillsets = models.TextField(blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Volunteer: {self.devotee.name}"
