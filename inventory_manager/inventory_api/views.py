from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from datetime import date
from .serializer import *


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeActions(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,employee_id):
        products = Assigned_Employee.objects.filter(employee=employee_id)
        product_return = []
        for product in products:
            if product.checked_out:
                product_return.append(product.product)
        return Response(ProductSerializer(product_return, many=True).data, status=status.HTTP_200_OK)



class StockHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,store_id):
        product_state_validation()
        try:
            products = []
            stock = Products.objects.filter(Storefront=store_id)
            for item in stock:
                if item.status.name != 'Sold' and item.status.name != 'Returning_From_Store':
                    products.append(item)
            return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)
        except:
            return Response(request.data,status=status.HTTP_400_BAD_REQUEST)



class EmployeeUnprotected(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        product_state_validation()
        product_model = ProductType.objects.all()
        status_type = Status.objects.all()
        request_type = RequestType.objects.all()
        list = {"products": ProductTypeSerializer(product_model, many=True).data,
                "status": StatusSerializer(status_type, many=True).data,
                "request": RequestTypeSerializer(request_type, many=True).data}
        return Response(list, status=status.HTTP_200_OK)


class EmployeeHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        employees = Employees.objects.all()
        return Response(EmployeeSerializer(employees, many=True).data, status=status.HTTP_200_OK)


class RoleHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        roles = Role.objects.all()
        return Response(RoleSerializer(roles, many=True).data,status=status.HTTP_200_OK)



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

class StoreHandler(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,manager_id):
        product_state_validation()
        try:
            store = Storefront.objects.get(manager_id=manager_id)
            return Response(StorefrontSerializer(store).data, status=status.HTTP_200_OK)
        except:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

class ProductHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, filter_type, filter_value):
        product_state_validation()

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
        product_state_validation()
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

def product_state_validation():
    products = Products.objects.all()
    for product in products:
        if product.status.name == 'Pending_Check_In':
            temp = Assigned_Employee.objects.filter(product_id=product.id)
            for employee in temp:
                if employee.checked_out:
                    employee.checked_out = False
                    employee.date_returned = date.today()
                    employee.save()



def status_key():
    possible_status = Status.objects.all()
    result = {}
    for state in possible_status:
        result[state.id]=state.name
    return result
