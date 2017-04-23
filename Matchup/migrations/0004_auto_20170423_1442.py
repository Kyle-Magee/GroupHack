# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matchup', '0003_auto_20170423_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='project_level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=13),
        ),
    ]
