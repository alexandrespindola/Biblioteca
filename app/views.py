#from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

# def hello_world(request):
#     return HttpResponse('Está funcionando!')

def home(request):
    return render(request, 'app/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'app/book_list.html', {'books': books})