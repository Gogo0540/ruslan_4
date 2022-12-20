from django.shortcuts import render
from book.models import Book


def list_book_view(request):
    book = Book.objects.all()
    return render(request, 'book.html', context={'book': book})

def detail_book_view(request, **kwargs):
    if request.method == 'GET':
        book = Book.objects.get(id=kwargs['id'])
        return render(request, 'detail_book.html',context={'book': book})
