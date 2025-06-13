from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book_images/')
    youtube_embed = models.TextField(blank=True, null=True)
    published_year = models.IntegerField()

    def average_rating(self):
        reviews = self.reviews_set.all()
        if reviews.exists():
            return round(sum(review.mark for review in reviews) / reviews.count(), 1)
        return 'Нет оценок'

    def __str__(self):
        return self.title


class Reviews(models.Model):
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(validators=[
        MinValueValidator(1, message='Оценка должна быть от 1 до 5'),
        MaxValueValidator(5, message='Оценка должна быть от 1 до 5')
    ])

    def __str__(self):
        return f'{self.author} - {self.choice_book}'