from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role = models.ForeignKey('Role', on_delete=models.RESTRICT, default=None, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, unique=True)


class Role(models.Model):
    name = models.CharField(max_length=50)


class Status(models.Model):
    name = models.CharField(max_length=50)
    available = models.BooleanField()


class Products(models.Model):
    hardware_version = models.CharField(max_length=50)
    employee_unit = models.BooleanField()
    status = models.ForeignKey('Status', on_delete=models.RESTRICT)
    model = models.ForeignKey('ProductType', on_delete=models.RESTRICT)
    Storefront = models.ForeignKey('Storefront', on_delete=models.RESTRICT, default=None, blank=True, null=True)
    Assigned_Employee = models.ManyToManyField(Employees, through='Assigned_Employee')


class ProductType(models.Model):
    name = models.CharField(max_length=50)

class Type(models.Model):
    name = models.CharField(max_length=50)


class Storefront(models.Model):
    manager = models.ForeignKey('Employees', on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)


class Assigned_Employee(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=True)
    date_returned = models.DateField(default=None, blank=True, null=True)


class Request(models.Model):
    product = models.ForeignKey('ProductType', on_delete=models.RESTRICT, default=None, blank=True, null=True)
    employee = models.ForeignKey('Employees', on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=1)
    priority = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(0)])
    type = models.ForeignKey('Type', on_delete=models.RESTRICT, default=None, null=True)
    justification = models.CharField(max_length=500, default=None, blank=True)
    approval = models.BooleanField(default=None, null=True)
    completed = models.BooleanField(default=None, null=True)
