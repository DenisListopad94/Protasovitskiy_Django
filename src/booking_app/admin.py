from .models import (
    Persons,
    HotelOwner,
    Hotels,
    Hobbies,
    Profile,
    BookOrderInfo,
    HotelsComment,
    User,
    PersonComment
)
from django.contrib import admin

# Register your models here.
admin.site.register(Persons)
admin.site.register(HotelOwner)
admin.site.register(Hotels)
admin.site.register(Hobbies)
admin.site.register(Profile)
admin.site.register(BookOrderInfo)
admin.site.register(HotelsComment)
admin.site.register(User)
admin.site.register(PersonComment)
