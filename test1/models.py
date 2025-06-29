from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    youtube_trailer = models.URLField()

    def average_rating(self):
        reviews = self.comments.all()
        if reviews.exists():
            return round(sum(r.mark for r in reviews) / reviews.count(), 1)
        return None

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    mark = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)