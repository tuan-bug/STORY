# Generated by Django 3.1.14 on 2023-12-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_order_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='detail',
        ),
        migrations.AddField(
            model_name='slide',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
