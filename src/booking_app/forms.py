from django import forms

from .models import User, HotelsComment, Profile, Hotels


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "age", "sex"]


class HotelsCommentForm(forms.ModelForm):
    class Meta:
        model = HotelsComment
        fields = ["comment", "hotel_rating", "hotels", "persons"]
        widgets = {
            "comment": forms.Textarea(attrs={"size": 500, 'class': 'special', "required": False})
        }


class ProfileAddForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo", "persons"]


class HotelAddForm(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = ["name", "stars", "address", "photo"]


