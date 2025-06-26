from django.shortcuts import render, get_object_or_404
from .models import Book
from reviews.models import Reviews
from django.core.paginator import Paginator
from statistics import mean

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3)  # 3 книги на страницу
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "books/book_list.html", {"page_obj": page_obj})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = Reviews.objects.filter(choice_book=book)
    marks = [r.mark for r in comments]
    average_mark = mean(marks) if marks else None
    return render(request, "books/book_detail.html", {
        "book": book,
        "comments": comments,
        "average_mark": average_mark
    })