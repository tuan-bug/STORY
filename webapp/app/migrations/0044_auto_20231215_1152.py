# Generated by Django 3.1.14 on 2023-12-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20231212_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='status',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
