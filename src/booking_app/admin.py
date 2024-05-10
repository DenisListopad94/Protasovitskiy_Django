from .models import (
    Persons,
    HotelOwner,
    Hotels,
    Hobbies,
    Profile,
    BookOrderInfo,
    HotelsComment
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
