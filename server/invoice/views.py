from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import InvoiceSerializer, InvoiceSerializerForCreate
from .models import Invoice
from django.http import JsonResponse
from book_item.models import Item
import json

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_permissions(self):
        if self.action == "create" or self.action == "update":
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = InvoiceSerializerForCreate
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]


    def create(self, request, *args, **kwargs):
        try:
            body = json.loads(request.body.decode())
            session_user = request.user.id

            if session_user != body['user']:
                return JsonResponse({
                    "fail": "You cannot generate invoices on behalf of this account, you are not the owner"
                }, status=403)

            user_invoices = Invoice.objects.filter(user=session_user, is_active=True)
            if len(user_invoices) >= 3:
                return JsonResponse({
                    "fail": "You cannot rent more than 3 items at once, make sure to return at least one of the items you own before another rent"
                }, status=403)

            item = Item.objects.get(pk=body['item'], is_available=True)
            item.is_available = False
            item.save()

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            invoice = Invoice.objects.last()
            return JsonResponse({
                "id": invoice.id,
                "uuid": invoice.uuid,
                "created_at": invoice.created_at,
                "days_to_return": invoice.days_to_return,
                "user": session_user,
                "item": body['item'],
                "is_item_returned": invoice.is_item_returned,
                "is_active": invoice.is_active,
            }, status=201 )
        except Exception as e:
            print(e)
            return JsonResponse({
                "fail": "No more availables copies of this book, try later"
            }, status=410 )
    
    def update(self, request, pk, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        try:
            session_user = request.user.id

            invoice = Invoice.objects.get(pk=pk, is_item_returned=False, is_active=True)
            if int(session_user) != int(invoice.user.id):
                return JsonResponse({
                    "fail": "You cant update this invoice status, you are not the owner"
                }, status=403)
            item = Item.objects.get(pk=invoice.item.id)
            invoice.is_item_returned = True
            invoice.is_active = False
            invoice.save()
            item.is_available = True
            item.save()

            return JsonResponse({
                "id": invoice.id,
                "uuid": invoice.uuid,
                "updated_at": invoice.updated_at,
                "user": session_user,
                "item": item.id,
                "is_item_returned": invoice.is_item_returned,
                "is_active": invoice.is_active,
            }, status=202 )

            
        except Exception as e:
            print(e)
            return JsonResponse({
                "fail": "This item does not exists or is already returned"
            }, status=410 )
