# Generated by Django 3.1.1 on 2020-10-10 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20201010_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detsale',
            name='prod',
        ),
        migrations.RemoveField(
            model_name='detsale',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cate',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='cli',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='DetSale',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]
