# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-20 12:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20161020_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 10, 20, 12, 33, 40, 162007, tzinfo=utc)),
        ),
    ]
