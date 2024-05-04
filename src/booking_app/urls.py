from django.urls import path
from .views import site_rules, all_establishments
urlpatterns = [
    path('site_rules/', site_rules),
    path('all_establishments/', all_establishments)
]
