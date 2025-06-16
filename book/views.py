from django.shortcuts import render, get_object_or_404
from .models import Book, Reviews
from .forms import ReviewForm
from django.db.models import Avg

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Reviews.objects.filter(choice_book=book)
    average_rating = reviews.aggregate(Avg('mark'))['mark__avg']
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.choice_book = book
            review.author = request.user
            review.save()
    else:
        form = ReviewForm()

    return render(request, 'book/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form
    })