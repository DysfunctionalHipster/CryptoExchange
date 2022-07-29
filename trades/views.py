from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from wires import serializers
from .models import Trade
from .serializers import TradeCreateSerializer, TradeUpdateSerializer
from user.models import User


@api_view(['GET', 'POST',])
@permission_classes([IsAuthenticated])
def open_position(request):
    trader = request.user
    trade = Trade(trader=trader)

    if request.method == 'POST':
        serializer = TradeCreateSerializer(trade, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH',])
@permission_classes([IsAuthenticated])
def close_position(request, id):

    try:
        trade = Trade.objects.get(id=id)
    except Trade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if trade.trader != user:
        return Response({'response': "You don't have permission to close this trade"})

    if request.method == 'PATCH':
        serializer = TradeUpdateSerializer(trade, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
