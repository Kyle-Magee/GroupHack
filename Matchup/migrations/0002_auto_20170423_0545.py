# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matchup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='languages',
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(to='Matchup.Language'),
        ),
    ]
