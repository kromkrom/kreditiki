# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kreddb', '0023_auto_20160920_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kreddb.CarModel'),
        ),
    ]
