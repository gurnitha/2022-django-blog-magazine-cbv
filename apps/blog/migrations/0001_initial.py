# Generated by Django 3.2.7 on 2022-01-22 06:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_slug', models.SlugField(max_length=225, unique=True, verbose_name='Url')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('tag_slug', models.SlugField(max_length=225, unique=True, verbose_name='Url')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tag',
                'ordering': ('tag_name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=255)),
                ('post_slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('post_content', models.TextField(blank=True)),
                ('post_publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('post_views', models.IntegerField(default=0, verbose_name='Times of viewed')),
                ('post_status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=15)),
                ('post_type', models.CharField(choices=[('featured', 'featured'), ('featured', 'featured')], default='latest', max_length=20)),
                ('is_editor_pick', models.BooleanField(default=False)),
                ('is_trending', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='accounts.author')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category')),
                ('tag_id', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-post_publish',),
            },
        ),
    ]
