# Generated by Django 4.2 on 2023-05-21 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_product_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
