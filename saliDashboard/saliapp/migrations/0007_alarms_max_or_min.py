# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saliapp', '0006_sensortype_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarms',
            name='max_or_min',
            field=models.BooleanField(default=False),
        ),
    ]
