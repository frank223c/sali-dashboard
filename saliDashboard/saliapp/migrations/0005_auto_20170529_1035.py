# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saliapp', '0004_auto_20170529_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cmpercompany',
            old_name='id_user',
            new_name='id_company',
        ),
    ]
