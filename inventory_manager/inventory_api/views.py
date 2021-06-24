from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializer import *

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Request_Handler(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        content = {"message":"hello world"}
        return Response(content, status=status.HTTP_200_OK)