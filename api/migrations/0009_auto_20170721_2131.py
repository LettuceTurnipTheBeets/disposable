# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 21:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170721_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('message', models.TextField(max_length=140)),
                ('time', models.DateTimeField(default=datetime.datetime(2017, 7, 21, 21, 31, 52, 880237))),
            ],
            options={
                'ordering': ('time',),
            },
        ),
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 21, 21, 31, 52, 878227)),
        ),
        migrations.AddField(
            model_name='chat',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Room'),
        ),
    ]
