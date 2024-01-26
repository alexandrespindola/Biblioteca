from django.shortcuts import render
# from .models import Book

def home(request):
    return render(request, 'app/home.html')

# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'app/book_list.html', {'books': books})



