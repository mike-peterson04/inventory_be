# Generated by Django 3.1.8 on 2021-07-03 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_api', '0018_auto_20210629_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storefront',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory_api.employees', unique=True),
        ),
    ]