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
            "first_name": "Primeiro nome",
            "last_name": "Sobrenome",
            "age": "Idade",
            "email": "E-mail",
            "address": "Endereço",
            "resides_in_sp": "Reside em SP",
            "event": "Evento",
            "time_confirmation": "Declaro que estou ciente de que o evento ocorrerá à noite",
        }
