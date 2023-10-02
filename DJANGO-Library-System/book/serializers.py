from rest_framework import serializers
from .models import Book
from book_item.serializers import ItemSerializer

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        depth = 1

class BookSerializerForRetrieve(serializers.ModelSerializer):
    
    items = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Book
        fields = '__all__'
        depth = 1

    def get_items(self, obj):
        items = obj.item_set.all()
        serializer = ItemSerializer(items, many = True)
        return serializer.data

class BookSerializerForCalling(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'image', 'is_active']