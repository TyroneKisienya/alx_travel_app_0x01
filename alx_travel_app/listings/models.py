from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    class roleType(models.TextChoices):
        GUEST = 'Guest', 'guest'
        HOST = 'Host', 'host'
        ADMIN = 'Admin', 'admin'

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    first_name = models.CharField(max_length=128, null= False)
    last_name = models.CharField(max_length=128, null= False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=128)
    role = models.CharField(choices=roleType, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
class Listing(models.Model):
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=128)
    location = models.CharField(max_length=128)
    pricepernight = models.DecimalField(decimal_places=2, max_digits=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True)

class Booking(models.Model):
    class statusType(models.TextChoices):
        PENDING = 'Pending', 'pending'
        CONFIRMED = 'Confirmed', 'confirmed'
        CANCELED = 'Canceled', 'canceled'

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True, null=False)
    end_date = models.DateTimeField(auto_created=True, null = False)
    status = models.CharField(choices=statusType, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    