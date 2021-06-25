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


class EmployeeHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # user = validate(request.auth.payload.user_id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


def validate(user):
    try:
        user = Employees.objects.get(user=user)
        return user
    except:
        return "Access not yet validated please check with your system administrator on request status"
