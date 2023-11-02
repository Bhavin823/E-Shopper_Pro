# Generated by Django 4.2.6 on 2023-10-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0001_initial'),
        ('order_app', '0004_ordermodel_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='order_item',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='order_item',
            field=models.ManyToManyField(to='cart_app.cartitemmodel'),
        ),
    ]
