from django.db import models


# Create your models here.
class Persons(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=SEX_PERSON)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class HotelOwner(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_PERSON)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Hotels(models.Model):
    name = models.CharField(max_length=40)
    stars = models.IntegerField(null=True)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    owners = models.ForeignKey(
        to="HotelOwner",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotels",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.name} {self.address}"


class Hobbies(models.Model):
    name = models.CharField(max_length=30)
    experience = models.IntegerField(null=True)
    owners = models.ManyToManyField(
        to="HotelOwner",
        related_name="hobbies"
    )
    persons = models.ManyToManyField(
        to="Persons",
        related_name="hobbies"
    )


class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True)
    id_card_number = models.IntegerField(null=True)
    serial = models.FloatField(null=True)
    persons = models.OneToOneField(
        to="Persons",
        on_delete=models.CASCADE,
        null=True,
        related_name="profile"
    )
    hotel_owners = models.OneToOneField(
        to="HotelOwner",
        on_delete=models.CASCADE,
        null=True,
        related_name="profile"
    )


class BookOrderInfo(models.Model):
    detail = models.CharField(max_length=200, null=True)
    time_order = models.DateTimeField(auto_now_add=True)
    persons = models.ForeignKey(
        to="Persons",
        on_delete=models.SET_NULL,
        null=True,
        related_name='booking_info'
    )
    hotels = models.ForeignKey(
        to="Hotels",
        on_delete=models.SET_NULL,
        null=True,
        related_name='booking_info'
    )


class HotelsComment(models.Model):
    comment = models.CharField(max_length=200, null=True)
    time_comment = models.DateTimeField(auto_now_add=True)
    hotels = models.ForeignKey(
        to="Hotels",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotel_comments"
    )
    persons = models.ForeignKey(
        to="Persons",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotel_comments"
    )

    def __str__(self):
        return f" {self.comment}"
