from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from . import models
from .serializers import WireCreateSerializer
from user.models import User
from .models import Wire


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def wire_transfer(request):
 
    owner = request.user
    wire = Wire(owner=owner)

    if request.method == 'POST':
        serializer = WireCreateSerializer(wire, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
