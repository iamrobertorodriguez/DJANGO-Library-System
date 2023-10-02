from dataclasses import fields
from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('user',)
        model = Invoice
        depth = 1

class InvoiceSerializerForCreate(serializers.ModelSerializer):
    class Meta:
        fields = ['user', 'item']
        model = Invoice

class InvoiceSerializerForUpdate(serializers.ModelSerializer):
    class Meta:
        fields = ['user', 'item']
        model = Invoice