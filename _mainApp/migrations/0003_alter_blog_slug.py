# Generated by Django 5.0 on 2024-01-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_mainApp', '0002_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
