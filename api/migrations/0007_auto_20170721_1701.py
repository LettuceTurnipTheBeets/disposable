# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 17:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170721_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 21, 17, 1, 57, 988502)),
        ),
    ]
