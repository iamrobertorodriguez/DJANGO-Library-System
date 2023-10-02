from django.db import models
from book.models import Book

# Create your models here.

class Item(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    is_available = models.BooleanField(
        default=True
    )