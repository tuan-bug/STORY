# Generated by Django 4.2.2 on 2023-08-24 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_payment_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemtemp',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ordertemp'),
        ),
    ]
