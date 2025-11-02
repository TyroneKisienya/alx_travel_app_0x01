from django.shortcuts import render
from .models import User, Listing, Booking
from .serializers import Userserializers, ListingSerializers, BookingSerializers
from rest_framework import status
from rest_framework import response

# Create your views here.
from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Welcome to the Listings API"})
