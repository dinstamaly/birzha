from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterAPIView, UserViewList

urlpatterns = [
    path('', UserViewList.as_view(), name='auth'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('jwt/', obtain_jwt_token),
    path('rest-auth/', include('rest_auth.urls')),
]
