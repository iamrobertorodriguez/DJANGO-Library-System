from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user.views import GetUserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/v1/getuser/', GetUserAPIView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/v1/", include("core.api.v1.urls")),
]
