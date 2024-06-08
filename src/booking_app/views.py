from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import UserModelForm, HotelsCommentForm, ProfileAddForm, HotelAddForm
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


@login_required(login_url="/admin/login/")
def all_establishments(request):
    return HttpResponse("Все заведения")


def home_view(request):
    return render(request=request,
                  template_name="home.html"
                  )


def hotels_view(request):
    context = {
        "hotels": Hotels.objects.all().prefetch_related("hotel_comments")
    }
    return render(request=request,
                  template_name="hotels.html",
                  context=context
                  )


class HotelsTemplateView(PermissionRequiredMixin, TemplateView):
    permission_required = ["booking_app.view_hotels"]
    template_name = "hotels.html"

    # @method_decorator(cache_page(30 * 60))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hotels"] = Hotels.objects.all()
        return context


def users_view(request):
    context = {
        "users": Persons.objects.all().prefetch_related("hobbies")
    }
    return render(request=request,
                  template_name="users.html",
                  context=context
                  )


class PersonsListView(PermissionRequiredMixin, ListView):
    permission_required = ["booking_app.view_persons"]
    template_name = "users.html"
    model = Persons
    # queryset = Persons.objects.all()
    context_object_name = "users"
    paginate_by = 7

    # @method_decorator(cache_page(30 * 60))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


@login_required(login_url="/admin/login/")
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


def user_add_form(request):
    if request.method == "POST":
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        return HttpResponseRedirect(reverse("users"))
    else:
        user_form = UserModelForm()
    context = {
        "form": user_form
    }

    return render(
        request=request,
        template_name="user_add_form.html",
        context=context
    )


class UserFormView(CreateView):
    template_name = "user_add_form.html"
    form_class = UserModelForm
    success_url = reverse_lazy("users")


def hotel_comment_add_form(request):
    if request.method == "POST":
        comment_form = HotelsCommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
        return HttpResponseRedirect(reverse("hotels"))
    else:
        comment_form = HotelsCommentForm()
    context = {
        "form": comment_form
    }

    return render(
        request=request,
        template_name="hotel_comment_add.html",
        context=context
    )


class HotelCommentFormView(CreateView):
    template_name = "hotel_comment_add.html"
    form_class = HotelsCommentForm
    success_url = reverse_lazy("hotels")


def profile_add_form(request):
    if request.method == "POST":
        profile_form = ProfileAddForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
        return HttpResponseRedirect(reverse("users"))
    else:
        profile_form = ProfileAddForm()
    context = {
        "form": profile_form
    }

    return render(
        request=request,
        template_name="profile_add_form.html",
        context=context
    )


class ProfileAddFormView(CreateView):
    template_name = "profile_add_form.html"
    form_class = ProfileAddForm
    success_url = reverse_lazy("users")


def hotels_add_form(request):
    if request.method == "POST":
        form = HotelAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("hotels"))
    else:
        form = HotelAddForm()
    context = {
        "form": form
    }
    return render(
        request=request,
        template_name="hotels_add_form.html",
        context=context
    )


class HotelsAddFormView(CreateView):
    template_name = "hotels_add_form.html"
    form_class = HotelAddForm
    success_url = reverse_lazy("hotels")
