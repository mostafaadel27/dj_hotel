# Generated by Django 3.2.6 on 2021-09-01 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
