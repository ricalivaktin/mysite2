# Generated by Django 5.0.1 on 2024-01-10 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_mainApp', '0008_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='_mainApp.category'),
        ),
    ]
