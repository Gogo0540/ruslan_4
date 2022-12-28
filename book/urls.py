from django.urls import path
from book.views import list_book_view, detail_book_view, book_create_view, update_book_view, delete_book_view

urlpatterns = [
    path('books/', list_book_view),
    path('books/<int:id>/', detail_book_view),
    path("create/book/", book_create_view),
    path('book/<int:id>/update/', update_book_view),
    path('book/<int:id>/delete/', delete_book_view),
]