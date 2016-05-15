# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kreddb', '0017_auto_20160515_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodynew',
            name='old_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='carmake',
            name='old_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='carmodelnew',
            name='old_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='enginenew',
            name='old_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='gearnew',
            name='old_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='generationnew',
            name='old_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='modificationnew',
            name='old_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bodynew',
            name='name',
            field=models.CharField(db_index=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='enginenew',
            name='name',
            field=models.CharField(db_index=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='gearnew',
            name='name',
            field=models.CharField(db_index=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='generationnew',
            name='name',
            field=models.CharField(db_index=True, max_length=127),
        ),
    ]
