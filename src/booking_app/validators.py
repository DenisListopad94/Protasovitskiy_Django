from django.core.exceptions import ValidationError


def validate_users_age(value):
    if int(value) < 18 or int(value) > 90:
        raise ValidationError(
            f"{value} must be more than 18 and less then 90",
        )
