# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('saliapp', '0005_auto_20170212_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SensorMeasurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saliapp.Measure')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saliapp.Sensor')),
            ],
        ),
        migrations.AddField(
            model_name='measure',
            name='members',
            field=models.ManyToManyField(through='saliapp.SensorMeasurements', to='saliapp.Sensor'),
        ),
    ]
