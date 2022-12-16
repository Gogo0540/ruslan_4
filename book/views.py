from django.shortcuts import render
from book.models import Book


def list_book_view(request):
    book = Book.objects.all()
    return render(request, 'book.html', context={'book': book})