from django.shortcuts import render, get_object_or_404
from .models import Book, Reviews

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews_set.all()
    average = book.average_rating()
    return render(request, 'book_detail.html', {
        'book': book,
        'reviews': reviews,
        'average': average
    })