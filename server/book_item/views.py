from rest_framework import viewsets
from .models import Item
from serializers import ItemSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

class BookItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(is_available = True)
    serializer_class = ItemSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]