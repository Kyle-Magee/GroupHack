# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=300, primary_key=True, serialize=False)),
                ('interests', models.CharField(max_length=300)),
                ('languages', models.CharField(max_length=300)),
                ('project_level', models.CharField(choices=[('BE', 'Beginner'), ('INT', 'Intermediate'), ('ADV', 'Advanced')], default='BE', max_length=13)),
            ],
        ),
    ]