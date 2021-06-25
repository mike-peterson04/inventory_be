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
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestApprover(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, request_id):
        request = Request.objects.get(pk=request_id)
        request.approval = True
        request.save()
        return Response(RequestSerializer(request).data, status=status.HTTP_200_OK)

    def post(self, request, request_id):
        request = Request.objects.get(pk=request_id)
        request.completed = True
        request.save()
        return Response(RequestSerializer(request).data, status=status.HTTP_200_OK)

    def delete(self,request,request_id):
        request = Request.objects.get(pk=request_id)
        request.completed = False
        request.approval = False
        request.save()
        return Response(RequestSerializer(request).data, status=status.HTTP_200_OK)


class ProductHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, filter_type, filter_value):

        if filter_type == 'id':
            products = Products.objects.filter(pk=filter_value)
        elif filter_type == 'hardware_version':
            products = Products.objects.filter(hardware_version=filter_value)
        elif filter_type == 'employee_unit':
            products = Products.objects.filter(employee_unit=filter_value)
        elif filter_type == 'status':
            products = Products.objects.filter(status=filter_value)
        elif filter_type == 'model':
            products = Products.objects.filter(model=filter_value)
        else:
            products = Products.objects.filter(Storefront=filter_value)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        try:
            product = Products.objects.get(pk=product_id)
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                product = serializer.update(product, request.data)
                return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


class ProductsHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        products = Products.objects.all()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StatusHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def validate(user):
#     try:
#         user = Employees.objects.get(user=user)
#         return user
#     except:
#         return "Access not yet validated please check with your system administrator on request status"
