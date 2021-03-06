# Generated by Django 3.1.8 on 2021-06-24 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
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
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_version', models.CharField(max_length=50)),
                ('employee_unit', models.BooleanField()),
                ('Storefront', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.storefront')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.type')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.status')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='role',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.role'),
        ),
        migrations.AddField(
            model_name='employees',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
