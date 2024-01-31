# Generated by Django 5.0 on 2024-01-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_chapter_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]