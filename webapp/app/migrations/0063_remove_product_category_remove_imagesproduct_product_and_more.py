# Generated by Django 5.0 on 2024-01-23 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='imagesproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ImagesProduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]