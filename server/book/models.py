from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import Category
from shelf.models import Shelf

default_book_img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/28c76cfe-f964-49b5-9a96-41825da0dd29/d45ldtj-22284684-8c3d-464e-b6d6-94d8813819ec.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI4Yzc2Y2ZlLWY5NjQtNDliNS05YTk2LTQxODI1ZGEwZGQyOVwvZDQ1bGR0ai0yMjI4NDY4NC04YzNkLTQ2NGUtYjZkNi05NGQ4ODEzODE5ZWMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.o-gIibMentMJilhCThKzA5sVPfEY16x_FVAQI70b2qw'

# Create your models here.

class Book(models.Model):
    title = models.CharField(
        _("title"),
        max_length=128
    )
    description = models.TextField(
        _("description")
    )
    author = models.CharField(
        _("author"),
        max_length=128
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Shelf,
        on_delete=models.CASCADE
    )
    image = models.URLField(
        max_length=1000,
        default=default_book_img
    )
    year = models.IntegerField(
        _("publication year")
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this book should be treated as active."
            "Unselect this instead of deleting books."
        ),
    )