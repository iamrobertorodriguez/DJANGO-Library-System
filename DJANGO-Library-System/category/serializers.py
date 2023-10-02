from rest_framework import serializers
from .models import Category
from book.serializers import BookSerializerForCalling

class CategorySerializer(serializers.ModelSerializer):

    books = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Category
        fields = '__all__'

    def get_books(self, obj):
        books = obj.book_set.all()
        serializer = BookSerializerForCalling(books, many = True)
        return serializer.data