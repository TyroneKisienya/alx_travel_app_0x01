from django.urls import path
from .views import Listingview

urlpatterns = [
    path('listing/',Listingview.as_view(), name='listing')
]