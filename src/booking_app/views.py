from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def site_rules(request):
    return HttpResponse("Правила сайта")


def all_establishments(request):
    return HttpResponse("Все заведения")


def home_view(request):
    return render(request=request,
                  template_name="home.html"
                  )


hotels = [
    {
        "name": "Bug",
        "address": "Bugskaya str.",
        "stars": 4,
    },
    {
        "name": "Goryn",
        "address": "Gorynskaya str.",
        "stars": 3,
    },
    {
        "name": "Lesnoi",
        "address": "Lesnaya str.",
        "stars": 2,
    },
]


def hotels_view(request):
    context = {
        "hotels": hotels
    }
    return render(request=request,
                  template_name="hotels.html",
                  context=context
                  )


users = [
    {
        "name": "Bob",
        "age": 20,
        "comment": "Good",
    },
    {
        "name": "Bill",
        "age": 22,
        "comment": "Bad",
    },
    {
        "name": "Ann",
        "age": 23,
        "comment": "Great",
    },
]


def users_view(request):
    context = {
        "users": users
    }
    return render(request=request,
                  template_name="users.html",
                  context=context
                  )


def user_comment_view(request):
    return render(request=request,
                  template_name="user_comment.html",
                  )
