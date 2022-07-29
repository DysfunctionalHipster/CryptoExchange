from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from user.models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'bio', 'avatar')