# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-16 16:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20161017_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 10, 16, 16, 16, 55, 156697, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='useridealstyle',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 10, 16, 16, 16, 55, 162697, tzinfo=utc)),
        ),
    ]