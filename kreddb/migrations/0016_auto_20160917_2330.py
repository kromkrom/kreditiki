# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kreddb', '0015_auto_20160825_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModelNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kreddb.Body')),
            ],
        ),
        migrations.RenameModel(
            old_name='CarModel',
            new_name='ModelFamily',
        ),
        migrations.RenameField(
            model_name='generation',
            old_name='car_model',
            new_name='model_family',
        ),
        migrations.RenameField(
            model_name='modification',
            old_name='car_model',
            new_name='model_family',
        ),
        migrations.AlterField(
            model_name='carimage',
            name='body',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kreddb.Body'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='generation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kreddb.Generation'),
        ),
        migrations.AlterUniqueTogether(
            name='generation',
            unique_together=set([('name', 'model_family', 'year_start', 'year_end')]),
        ),
        migrations.AddField(
            model_name='carmodelnew',
            name='generation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kreddb.Generation'),
        ),
        migrations.AddField(
            model_name='carimage',
            name='car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kreddb.CarModelNew'),
        ),
    ]
