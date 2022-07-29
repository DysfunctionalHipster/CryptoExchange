from rest_framework import serializers
from .models import Trade

class TradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('id', 'quantity', 'symbol')

class TradeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('id', 'open')

