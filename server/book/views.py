from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer, BookSerializerForRetrieve
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_active = True)
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = {
        'title',
        'author',
        'year',
        'description'
    }

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]
        elif self.action == "retrieve":
            self.permission_classes = [AllowAny]
            self.serializer_class = BookSerializerForRetrieve
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]