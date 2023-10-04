from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# https://docs.djangoproject.com/en/4.0/ref/validators/

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def starts_with_s(value):
    if value[0] != 'm':
        # raise forms.ValidationError("name Should Start with 'M'")
        raise forms.ValidationError(f"{value} Should Start with 'M'")


class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[starts_with_s])
    email = forms.EmailField()
    even_field = forms.IntegerField(validators=[validate_even])