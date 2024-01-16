from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('inscricao/', views.registration, name='registration'),
    path('registration_complete/', views.registration_complete, name='registration_complete'),
    path('', views.event_list, name='event_list'),
]