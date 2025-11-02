from .models import User, Listing, Booking
from rest_framework import serializers

class Userserializers(serializers.ModelSerializer):
    model = User
    fields = '__all__'

    extra_kwargs = {
        'role': {'default': User.roleType.GUEST}
    }

class ListingSerializers(serializers.ModelSerializer):
    model = Listing
    fields = '__all__'

class BookingSerializers(serializers.ModelSerializer):
    model = Booking
    fields = '__all__'

    extra_kwargs = {
        'status': {'default': Booking.statusType.PENDING}
    }