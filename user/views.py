from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from requests import request
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserCreateSerializer


# @api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def user_edit(request):
 
#     account = request.user

#     if request.method == 'GET':

#         serializer = WireCreateSerializer(wire, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserCreate(generics.CreateAPIView): # * Profile Registration 
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    pass 

@permission_classes([IsAuthenticated])
class UserDetail(generics.RetrieveUpdateAPIView): # * Profile Registration 
    queryset = User.objects.get(pk=1)
    serializer_class = UserSerializer
    pass 