# Generated by Django 3.1.8 on 2021-06-28 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_api', '0016_storeinventory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StoreInventory',
        ),
    ]
