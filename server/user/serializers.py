from rest_framework import serializers
from .models import User
from invoice.serializers import InvoiceSerializer
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        return super(UserSerializer, self).create(validate_data)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'is_superuser': {
                'write_only': True
            },
            'is_staff': {
                'write_only': True
            },
            'groups': {
                'write_only': True
            },
            'user_permissions': {
                'write_only': True
            }
        }

class UserSerializerForRetrieve(serializers.ModelSerializer):

    invoices = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['invoices', 
            'last_login', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'address', 
            'phone']

    def get_invoices(self, obj):
        invoices = obj.invoice_set.all()
        serializer = InvoiceSerializer(invoices, many = True)
        return serializer.data
