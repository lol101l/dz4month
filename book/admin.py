
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year', 'genre')  # Показывать в списке
    search_fields = ('title', 'author')  # Строка поиска
    list_filter = ('genre', 'published_year')  # Фильтрация сбоку

admin.site.register(Book, BookAdmin)