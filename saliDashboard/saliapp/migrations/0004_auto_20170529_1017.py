# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saliapp', '0003_sensor_cam_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CMPerUsers',
            new_name='CMPerCompany',
        ),
    ]
