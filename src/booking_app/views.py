from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Hotels,
    User,
    Persons,
    Room,
    Booking
)
from django.db import transaction
from datetime import datetime


# Create your views here.
def site_rules(request):
    return HttpResponse("Правила сайта")


def all_establishments(request):
    return HttpResponse("Все заведения")


def home_view(request):
    return render(request=request,
                  template_name="home.html"
                  )


def hotels_view(request):
    context = {
        "hotels": Hotels.objects.filter(stars=5).prefetch_related("hotel_comments")
    }
    return render(request=request,
                  template_name="hotels.html",
                  context=context
                  )


def users_view(request):
    context = {
        "users": Persons.objects.all().prefetch_related("hobbies")
    }
    return render(request=request,
                  template_name="users.html",
                  context=context
                  )


def user_comment_view(request):
    return render(request=request,
                  template_name="user_comment.html",
                  )


@transaction.atomic
def book_room(request, hotel_name, user_id, room_number):
    if request.method == 'POST':
        try:
            hotel = Hotels.objects.get(name=hotel_name)
        except Hotels.DoesNotExist:
            return HttpResponse('Hotel with this name not exist', status=404)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return HttpResponse('User with this ID not exist', status=404)

        try:
            room = Room.objects.get(hotel=hotel, number=room_number)
        except Room.DoesNotExist:
            return HttpResponse('Room with this number not exist in this hotel', status=404)

        if room.is_booked:
            return HttpResponse('This room is booked', status=400)

        room.is_booked = True
        room.save()

        booking = Booking(
            room=room,
            start_date=datetime.now().date(),
            end_date=datetime.max.date(),
            customer_full_name=f"{user.first_name} {user.last_name}"
        )
        booking.save()

        return HttpResponse('This room is successfully booked')

    return render(
        request,
        'room_booking.html',
        {
            'hotel_name': hotel_name,
            'user_id': user_id,
            'room_number': room_number
        }
    )
