# Generated by Django 4.2 on 2023-05-22 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
