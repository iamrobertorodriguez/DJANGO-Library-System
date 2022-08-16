from .models import User
from .serializers import UserSerializer, UserSerializerForRetrieve
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = UserSerializerForRetrieve
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['is_staff'] = False
        request.data['is_superuser'] = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if int(request.user.id) != int(pk):
            return JsonResponse({
                "fail": "You are not the owner of the data you are asking for"
            }, status=403)

        return Response(serializer.data)

class GetUserAPIView(APIView):
    def get(self, request):
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            user, token = response
            session_user = User.objects.get(pk=request.user.id)
            return JsonResponse({
                "token": token.payload,
                "user": {
                    "first_name": session_user.first_name,
                    "last_name": session_user.last_name,
                    "username": session_user.username,
                    "email": session_user.email,
                    "phone": session_user.phone,
                    "address": session_user.address
                }
            }, status=200)
        else:
            return JsonResponse({
                "fail": "no token is provided in the header or the header is missing"
            }, status=401)