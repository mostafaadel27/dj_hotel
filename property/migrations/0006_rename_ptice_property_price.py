# Generated by Django 3.2.6 on 2021-09-02 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_place_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='ptice',
            new_name='price',
        ),
    ]
