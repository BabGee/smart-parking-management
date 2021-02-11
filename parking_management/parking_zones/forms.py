import datetime
from django.forms import ModelForm, DateInput, TextInput, ValidationError
from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = ['customer',]
        # Validating form fields using widgets
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'finish_date': DateInput(attrs={'type': 'date'}),
            'plate_number': TextInput(attrs={'pattern': '^K[A-Z]{2}[0-9]{3}[A-Z]$', 'title': 'Enter a valid parking space number'}),
            'phone_number': TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter digits only '}),
        }

# Additional custom validator for start_date / finish_date fields
    def clean(self):
        data = self.cleaned_data
        start_date = data['start_date']
        finish_date = data['finish_date']

        if start_date > finish_date:
            raise ValidationError('Wrong start and finish dates.')

        if start_date < datetime.date.today():
            raise ValidationError('Start date in the past.')

        return data


# class ParkingSpaceForm(ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['plate_number']
#         widgets = {
#             'plate_number': TextInput(attrs={'pattern': '[1-7]+', 'title': 'Enter a valid plate_number'})
#         }

