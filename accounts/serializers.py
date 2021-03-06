import datetime

from django.conf import settings
from django.utils import timezone
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.reverse import reverse as api_reverse
from .models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']


class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'user_type',
            'uri'
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-user:user-detail", kwargs={"username": obj.username}, request=request)


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token     = serializers.SerializerMethodField(read_only=True)
    message   = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'user_type',
            'balance',
            'token',

            'message'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_message(self, obj):
        return "thankssss"

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this name already exists")
        return value

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Password must match.")
        return data

    def create(self, validated_data):
        print(validated_data)

        user_obj = User(
            username=validated_data.get('username'),
            user_type=validated_data.get('user_type'),
            balance=validated_data.get('balance'),


        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = True
        user_obj.save()
        return user_obj
