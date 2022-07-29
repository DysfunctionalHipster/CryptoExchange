from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def welcome(request, *args, **kwargs):
    return Response(data='Welcome to CryptoExchange', status=status.HTTP_200_OK)