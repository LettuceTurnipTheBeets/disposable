# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 16:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170721_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='duration',
        ),
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 21, 16, 9, 52, 977002)),
        ),
    ]
