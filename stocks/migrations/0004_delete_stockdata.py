# Generated by Django 3.2.6 on 2021-09-03 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_alter_stockdata_stock'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StockData',
        ),
    ]
