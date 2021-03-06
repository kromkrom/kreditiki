# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kreddb', '0003_auto_20160606_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='group',
            field=models.CharField(choices=[('SF', 'Безопасность'), ('CF', 'Комфорт'), ('VW', 'Обзор'), ('IN', 'Салон'), ('MM', 'Мультимедиа'), ('CJ', 'Защита от угона'), ('EX', 'Экстерьер')], max_length=2),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='rank',
            field=models.SmallIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feature',
            name='group',
            field=models.CharField(choices=[('GE', 'Общая информация'), ('SF', 'Безопасность'), ('EX', 'Эксплуатационные показатели'), ('EN', 'Двигатель'), ('GR', 'Трансмиссия'), ('SZ', 'Размеры в мм'), ('VM', 'Объем и масса'), ('SB', 'Подвеска и тормоза')], max_length=2),
        ),
        migrations.AlterField(
            model_name='feature',
            name='rank',
            field=models.SmallIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='equipment',
            unique_together=set([('group', 'rank')]),
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set([('group', 'rank')]),
        ),
    ]
