# Generated by Django 5.0 on 2024-01-23 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0057_delete_paymentrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
