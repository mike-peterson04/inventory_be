# Generated by Django 3.1.8 on 2021-06-28 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_api', '0013_auto_20210627_1506'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='RequestType',
        ),
    ]