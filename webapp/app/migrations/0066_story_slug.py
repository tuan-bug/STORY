# Generated by Django 5.0 on 2024-01-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_remove_story_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
