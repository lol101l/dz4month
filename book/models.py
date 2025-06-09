from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    cover_image = models.ImageField(upload_to='media/book/')
    youtube_link = models.URLField(blank=True, null=True, help_text="Embed ссылка с YouTube")

    def __str__(self):
        return self.title