from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def site_rules(request):
    return HttpResponse("Правила сайта")


def all_establishments(request):
    return HttpResponse("Все заведения")
