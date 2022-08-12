from django.db import models
from user.models import User
from book_item.models import Item
import uuid

# Create your models here.

class Invoice(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4())
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    days_to_return = models.IntegerField(default=7)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    is_item_returned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)