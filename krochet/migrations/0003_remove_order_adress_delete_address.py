# Generated by Django 4.1.6 on 2023-02-11 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krochet', '0002_address_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='adress',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
