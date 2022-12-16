from django.urls import path
from book.views import list_book_view

urlpatterns = [
    path('books/', list_book_view)
]