# Generated by Django 4.1.5 on 2023-02-08 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_product_pic1_alter_product_pic2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='pic4',
            new_name='pic',
        ),
    ]
