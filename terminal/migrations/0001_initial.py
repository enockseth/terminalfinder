# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Operator',
                'verbose_name_plural': 'Operators',
            },
        ),
    ]