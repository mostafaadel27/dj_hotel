# Generated by Django 3.2.6 on 2021-09-01 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_remove_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(upload_to='properity'),
        ),
    ]
