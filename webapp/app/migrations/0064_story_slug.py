# Generated by Django 5.0 on 2024-01-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_remove_product_category_remove_imagesproduct_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
