from django.contrib import admin
from .models import Book, Reviews

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['choice_book', 'author', 'mark']