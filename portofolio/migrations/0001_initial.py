# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_author', models.CharField(max_length=100)),
                ('article_title', models.CharField(max_length=255, verbose_name='Title')),
                ('article_slug', models.CharField(max_length=255, verbose_name='Slug')),
                ('article_content', models.TextField(verbose_name='Content')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Category')),
                ('category_slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('category_desc', models.TextField(verbose_name='Description')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, verbose_name='Name')),
                ('project_date', models.DateField(verbose_name='Date')),
                ('project_url', models.URLField(max_length=225, verbose_name='Project URL')),
                ('project_thumb', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Thumbnail')),
                ('project_desc', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_name', models.CharField(max_length=100)),
                ('setting_value', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.Category'),
        ),
    ]
