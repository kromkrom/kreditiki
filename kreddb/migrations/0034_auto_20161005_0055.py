# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kreddb', '0033_auto_20161003_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='model_family',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kreddb.ModelFamily'),
            preserve_default=False,
        ),
    ]
