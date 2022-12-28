from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from book.models import Book
from .forms import BookForm
from . import models, forms


def list_book_view(request):
    if request.method == "GET":
        book = Book.objects.all()
        return render(request, 'book.html', context={'book': book})


def detail_book_view(request, **kwargs):
    if request.method == 'GET':
        book = Book.objects.get(id=kwargs['id'])
        return render(request, 'detail_book.html', context={'book': book})


def book_create_view(request):
    if request.method == 'GET':
        data = {
            'form': BookForm
        }
        return render(request, 'book_create.html', context=data)
    elif request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        form.save()

        return HttpResponse('книга успешно добавлена')


def update_book_view(request, id):
    show_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Книга успешно обновлена</h1>')
    else:
        form = forms.BookForm(instance=show_object)
    return render(request, 'book_update.html', {'form': form, 'object': show_object})

def delete_book_view(request, id):
    show_object = get_object_or_404(models.Book, id=id)
    show_object.delete()
    return HttpResponse('<h1>Книга успешна удалена</h1>')
