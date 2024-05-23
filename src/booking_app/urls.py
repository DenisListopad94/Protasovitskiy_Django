from django.urls import path
from .views import (
    site_rules,
    all_establishments,
    home_view,
    user_comment_view,
    hotels_view,
    users_view,
    book_room,
    user_add_form,
    hotel_comment_add_form,
    HotelsTemplateView,
    PersonsListView,
    UserFormView,
    HotelCommentFormView,
)

urlpatterns = [
    path('site_rules/', site_rules),
    path('all_establishments/', all_establishments),
    path('home/', home_view, name='home'),
    path('user_comment/', user_comment_view, name='user_comment'),
    path('hotels/', HotelsTemplateView.as_view(), name='hotels'),
    path('users/', PersonsListView.as_view(), name='users'),
    path('book/<str:hotel_name>/<int:user_id>/<str:room_number>/', book_room, name='book_room'),
    path('user_add', UserFormView.as_view(), name="user_add"),
    path('comment_add', HotelCommentFormView.as_view(), name="comment_add"),
]
