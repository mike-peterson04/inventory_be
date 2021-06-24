from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employees, Role, Status, Products, Type, Storefront, AssignedProducts


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


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class StorefrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storefront
        fields = ['id', 'manager', 'name']


class AssignedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedProducts
        fields = ['id', 'employee', 'product', 'checked_out', 'date_returned']


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self,validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        user = User(**validated_data)
        if password == password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save