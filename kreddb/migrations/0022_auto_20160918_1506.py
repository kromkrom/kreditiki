# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kreddb', '0021_carmodel_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='do_body_override',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='do_generation_override',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='do_name_override',
            field=models.BooleanField(default=False),
        ),
    ]