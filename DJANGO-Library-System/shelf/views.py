from .models import Shelf
from rest_framework import viewsets
from .serializers import ShelfSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]