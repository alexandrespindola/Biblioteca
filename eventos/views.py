from django.db import connections, transaction
from django.shortcuts import render, redirect
from .forms import ParticipantForm
from .models import Participant
from .models import Event
from .models import Registration
from django.core.mail import send_mail

@transaction.atomic()

# Registro de participantes
def registration(request):
    try:
        connections['default'].ensure_connection()
    except Exception as e:
        return render(request, 'eventos/inscricao.html', {'form': ParticipantForm(), 'error': 'Não foi possível conectar ao banco de dados: {}'.format(e)})
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            if Participant.objects.count() >= 50:
                return render(request, 'eventos/inscricao.html', {'form': form, 'error': 'Infelizmente o limite de vagas para este evento está esgotado.'})
            participant = form.save(commit=False)
            if participant.age < 18 or not participant.resides_in_sp or not participant.time_confirmation:
                return render(request, 'eventos/inscricao.html', {'form': form, 'error': 'Desculpe, você não preenche as condições para inscrição no evento.'})
            participant.save()

            send_mail(
                'Confirmação de inscrição no evento',
                'Obrigado por se inscrever no nosso evento!',
                'dev@mercurioseo.com',
                [participant.email],
                fail_silently=False,
            )

            return redirect('eventos:registration_complete') 
    else:
        form = ParticipantForm()
    return render(request, 'eventos/inscricao.html', {'form': form})

# Registro completo - Sucesso
def registration_complete(request):
    return render(request, 'eventos/registration_complete.html')

# Lista de eventos
def event_list(request):
    events = Event.objects.all()
    return render(request, 'eventos/event_list.html', {'events': events})