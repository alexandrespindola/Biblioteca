from django import forms
from .models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            "first_name",
            "last_name",
            "age",
            "email",
            "address",
            "resides_in_sp",
            "event",
            "time_confirmation",
        ]
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "age": "Age",
            "email": "E-mail",
            "address": "Address",
            "resides_in_sp": "Resides in São Paulo",
            "event": "Event",
            "time_confirmation": "I declare that I am aware that the event will take place at night",
        }
