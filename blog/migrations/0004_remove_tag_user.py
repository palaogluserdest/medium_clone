# Generated by Django 4.1.7 on 2023-04-12 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_post_blogpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
    ]
