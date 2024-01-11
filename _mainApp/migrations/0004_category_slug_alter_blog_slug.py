# Generated by Django 5.0 on 2024-01-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_mainApp', '0003_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]