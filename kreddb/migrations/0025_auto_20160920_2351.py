# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 20:51
from __future__ import unicode_literals

from django.db import migrations


def update_car_info(apps, schema_editor):
    CarModel = apps.get_model("kreddb", "CarModel")
    CarInfo = apps.get_model("kreddb", "CarInfo")
    for car_info in CarInfo.objects.all():
        car_model, _ = CarModel.objects.get_or_create(
            generation=car_info.generation,
            body=car_info.body
        )
        car_info.car_model = car_model
        car_info.save()


class Migration(migrations.Migration):

    dependencies = [
        ('kreddb', '0024_auto_20160920_2345'),
    ]

    operations = [
        migrations.RunPython(update_car_info),
    ]
