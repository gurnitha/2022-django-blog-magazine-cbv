# Generated by Django 3.2.7 on 2022-01-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220122_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_editor_pick',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_trending',
            field=models.BooleanField(default=False),
        ),
    ]
