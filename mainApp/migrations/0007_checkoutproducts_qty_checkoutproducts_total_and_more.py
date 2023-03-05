# Generated by Django 4.1.5 on 2023-02-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproducts',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='checkoutproducts',
            name='total',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkout',
            name='orderstatus',
            field=models.IntegerField(choices=[(0, 'Order Placed'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Redy To Ship'), (4, 'Shipped'), (5, 'Out For Delivery'), (6, 'Delivered'), (7, 'Cancelled')], default=0),
        ),
    ]
