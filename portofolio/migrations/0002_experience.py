# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0001_initial'),
    ]

    operations = [
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
    ]
