from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        _("category name"),
        max_length=128,
        unique=True,
        error_messages={
            "unique": _("A category with that name already exists."),
        }
    )
    description = models.TextField(
        _("description")
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this category should be treated as active."
            "Unselect this instead of deleting categories."
        ),
    )