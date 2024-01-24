from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Validation for profile title
def validate_profile_title(value):
    if value <= 5 or value > 50:
        raise ValidationError(
            _("%(value)s is not a valid profile title.")
        )
    return value


def validate_profile_email(value):
    if value <= 5 or value > 50:
        raise ValidationError(
            _("%(value)s is not a valid profile email.")
        )

