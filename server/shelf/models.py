from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Shelf(models.Model):
    location = models.CharField(
        _("shelf location"),
        max_length=3,
        unique=True,
        error_messages={
            "unique": _("A shelf with that location already exists."),
        }
    )