from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework_jwt.settings import api_settings

from .serializers import UserRegisterSerializer, UserPublicSerializer
from .permissions import AnonPermissionOnly
from .models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class UserViewList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer


class RegisterAPIView(CreateAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}