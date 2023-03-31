from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'phone',
            'name_on_card',
            'card_number',
            'expiration_date',
            'year',
            'ccv',
        )