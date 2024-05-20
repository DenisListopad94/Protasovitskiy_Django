from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotels
from .models import Persons


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
