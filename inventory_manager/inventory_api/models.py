from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role = models.ForeignKey('Role', on_delete=models.RESTRICT, default=None, blank=True)


class Role(models.Model):
    name = models.CharField(max_length=50)


class Status(models.Model):
    name= models.CharField(max_length=50)
    available = models.BooleanField()


class Products(models.Model):
    hardware_version = models.CharField(max_length=50)
    employee_unit = models.BooleanField()
    status = models.ForeignKey('Status', on_delete=models.RESTRICT)
    model = models.ForeignKey('Type', on_delete=models.RESTRICT)
    Storefront = models.ForeignKey('Storefront', on_delete=models.RESTRICT)


class Type(models.Model):
    name = models.CharField(max_length=50)

class Storefront(models.Model):
    manager = models.ForeignKey('Employees', on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)

