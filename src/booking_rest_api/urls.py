from django.urls import path
from .views import HotelOwnerList, HotelOwnerDetail

urlpatterns = [
    path('hotel_owners/', HotelOwnerList.as_view(), name='hotel_owner_list'),
    path('hotel_owners/<int:pk>/', HotelOwnerDetail.as_view(), name='hotel_owner_detail'),
]