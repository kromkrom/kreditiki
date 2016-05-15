# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kreddb', '0014_auto_20150916_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mark',
            options={'managed': False, 'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='generation',
            name='car_model',
            field=models.ForeignKey(db_column='model_id', on_delete=django.db.models.deletion.CASCADE, to='kreddb.CarModel'),
        ),
        migrations.AlterField(
            model_name='modification',
            name='car_model',
            field=models.ForeignKey(db_column='model_id', on_delete=django.db.models.deletion.CASCADE, to='kreddb.CarModel'),
        ),
    ]
