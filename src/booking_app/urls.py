from django.urls import path
from .views import (
    site_rules,
    all_establishments,
    home_view,
    user_comment_view,
    hotels_view,
    users_view,
)
urlpatterns = [
    path('site_rules/', site_rules),
    path('all_establishments/', all_establishments),
    path('home/', home_view, name='home'),
    path('user_comment/', user_comment_view, name='user_comment'),
    path('hotels/', hotels_view, name='hotels'),
    path('users/', users_view, name='users'),
]
