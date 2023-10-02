from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import AllowAny, IsAdminUser

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active = True)
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]