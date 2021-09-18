# Generated by Django 3.2.6 on 2021-09-01 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='settings/')),
                ('addrees', models.TextField(max_length=1000)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(max_length=1000)),
                ('facebook', models.URLField(max_length=300)),
                ('twitter', models.URLField(max_length=300)),
                ('instgram', models.URLField(max_length=300)),
            ],
        ),
    ]