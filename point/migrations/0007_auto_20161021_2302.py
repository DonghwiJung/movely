# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-21 14:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0006_auto_20161021_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointhistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='point_histories', to=settings.AUTH_USER_MODEL),
        ),
    ]