from django.shortcuts import render
from .models import Listing, Booking
from .serializers import ListingSerializers, BookingSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from django.http import JsonResponse

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def listing_list(request):
    if request.method == 'GET':
        listing = Listing.objects.all()
        serializer = ListingSerializers(listing, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ListingSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = ListingSerializers(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

def index(request):
    return JsonResponse({"message": "Welcome to the Listings API"})
