# Generated by Django 3.1.14 on 2023-11-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20231113_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
