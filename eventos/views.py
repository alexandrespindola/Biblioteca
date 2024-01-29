from django.db import connections, transaction
from django.shortcuts import render, redirect
from .forms import ParticipantForm
from .models import Participant
from .models import Event
from .models import Registration
from django.core.mail import send_mail
from .models import send_confirmation_email

@transaction.atomic()

# Participant registration
def registration(request):
    try:
        connections['default'].ensure_connection()
    except Exception as e:
        return render(request, 'eventos/registration.html', {'form': ParticipantForm(), 'error': 'Não foi possível conectar ao banco de dados: {}'.format(e)})
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            if Participant.objects.count() >= 50:
                return render(request, 'eventos/registration.html', {'form': form, 'error': 'Unfortunately, the space limit for this event is sold out..'})
            participant = form.save(commit=False)
            if participant.age < 18 or not participant.resides_in_sp or not participant.time_confirmation:
                return render(request, 'eventos/registration.html', {'form': form, 'error': 'Sorry, you do not meet the conditions to register for the event.'})
            participant.save()

            send_confirmation_email(participant)

            return redirect('eventos:registration_complete') 
    else:
        form = ParticipantForm()
    return render(request, 'eventos/registration.html', {'form': form})

# Complete Registration - Success
def registration_complete(request):
    return render(request, 'eventos/registration_complete.html')

# Event list
def event_list(request):
    events = Event.objects.all()
    return render(request, 'eventos/event_list.html', {'events': events})