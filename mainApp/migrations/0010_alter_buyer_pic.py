# Generated by Django 4.1.5 on 2023-02-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
    ]
