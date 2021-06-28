# Generated by Django 3.1.8 on 2021-06-27 21:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory_api', '0012_auto_20210627_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigned_Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_out', models.BooleanField(default=True)),
                ('date_returned', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Storefront',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('priority', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('justification', models.CharField(blank=True, default=None, max_length=500)),
                ('approval', models.BooleanField(default=None, null=True)),
                ('completed', models.BooleanField(default=None, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.employees')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.producttype')),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.type')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_version', models.CharField(max_length=50)),
                ('employee_unit', models.BooleanField()),
                ('Assigned_Employee', models.ManyToManyField(through='inventory_api.Assigned_Employee', to='inventory_api.Employees')),
                ('Storefront', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.storefront')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.producttype')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.status')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='role',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.role'),
        ),
        migrations.AddField(
            model_name='employees',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AddField(
            model_name='assigned_employee',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_api.employees'),
        ),
        migrations.AddField(
            model_name='assigned_employee',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_api.products'),
        ),
    ]