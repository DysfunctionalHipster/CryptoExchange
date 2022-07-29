from rest_framework import serializers
from user.models import User
from .models import Wire

class WireCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wire
        fields = ('id', 'owner', 'amount', 'withdrawal')