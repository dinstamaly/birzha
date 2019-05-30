from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView

from accounts.permissions import IsOwnerOrReadOnly, IsLoggedInUserOrAdmin
from accounts.user.serializers import UserDetailSerializer
from ..models import User


class UserDeatilAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = "username"

    def get_serializer_context(self):
        return {'request': self.request}


# class UserProfileUpdate(UpdateAPIView):
#     # authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (IsLoggedInUserOrAdmin)
#     serializer_class = UserDetailSerializer
#
#     def get_object(self):
#         return User.objects.get(user=self.request.user)

