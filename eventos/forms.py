from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'age', 'email', 'address', 'resides_in_sp', 'time_confirmation', 'event']