from rest_framework import serializers
from .models import Shelf
from book.serializers import BookSerializerForCalling

class ShelfSerializer(serializers.ModelSerializer):

    books = serializers.SerializerMethodField(read_only = True)

    class Meta:
        fields = '__all__'
        model = Shelf

    def get_books(self, obj):
        books = obj.book_set.all()
        serializer = BookSerializerForCalling(books, many=True)
        return serializer.data
