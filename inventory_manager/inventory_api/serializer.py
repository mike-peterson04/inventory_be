from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'name', 'email', 'role', 'user']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'available']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'hardware_version', 'employee_unit', 'status', 'model', 'Storefront']

    def update(self, instance, validated_data):
        instance.hardware_version = validated_data.get('hardware_version', instance.hardware_version)
        instance.employee_unit = validated_data.get('employee_unit', instance.employee_unit)
        instance.model_id = validated_data.get('model', instance.model)
        instance.Storefront_id = validated_data.get('Storefront', instance.Storefront)
        instance.hardware_version = validated_data.get('hardware_version', instance.hardware_version)
        instance.status_id = validated_data.get('status', instance.status)
        instance.save()
        return instance


class RequestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestType
        fields = ['id', 'name', 'access']

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']

class StorefrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storefront
        fields = ['id', 'manager', 'name']


class AssignedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assigned_Employee
        fields = ['id', 'employee', 'product', 'checked_out', 'date_returned']


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        user = User(**validated_data)
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'product', 'employee', 'quantity', 'priority', 'type', 'justification', 'approval', 'completed']
