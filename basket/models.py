from django.db import models
from django.core.validators import MaxValueValidator
from book.models import Book

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    card_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999999999)])
    books = models.ManyToManyField(Book)
    status = models.CharField(max_length=20, choices=[('confirmed', 'Подтвержден'), ('unconfirmed', 'Не подтвержден')])

    def __str__(self):
        return f"Заказ от {self.full_name}"