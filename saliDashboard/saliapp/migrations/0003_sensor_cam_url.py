# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saliapp', '0002_auto_20170502_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='cam_url',
            field=models.CharField(blank=True, max_length=228),
        ),
    ]