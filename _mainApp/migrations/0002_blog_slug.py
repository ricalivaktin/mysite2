# Generated by Django 5.0 on 2024-01-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]