# Generated by Django 5.0 on 2024-01-23 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_story_likes_alter_story_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentRecord',
        ),
    ]
