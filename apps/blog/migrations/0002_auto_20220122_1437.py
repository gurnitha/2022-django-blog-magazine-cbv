# Generated by Django 3.2.7 on 2022-01-22 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_editor_pick',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_trending',
        ),
    ]
