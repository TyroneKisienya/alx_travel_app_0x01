from django.shortcuts import render
from .models import Listing, Booking
from .serializers import ListingSerializers, BookingSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

# Create your views here.

class Listingview(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                listing = Listing.objects.get(pk=pk)
                serializer = ListingSerializers(listing)
                return Response(serializer.data)
            except Listing.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        listing = Listing.objects.all()
        serializer = ListingSerializers(listing, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ListingSerializers(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            listing = Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListingSerializers(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            listing = Listing.objects.get(pk=pk)
            listing.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except listing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)     
