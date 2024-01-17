from django.db import models

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    vacancies_limit = models.IntegerField()
    city = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title

    @property
    def available_slots(self):
        registrations = Registration.objects.filter(event=self).count()
        return self.vacancies_limit - registrations


class Participant(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, blank=False, null=False, default='')
    resides_in_sp = models.BooleanField()
    time_confirmation = models.BooleanField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.participant.first_name} - {self.event.title}'
