# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20171116_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventomes',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='eventomes',
            name='titulo',
            field=models.CharField(default='Titulo do evento', max_length=100, unique=True),
        ),
    ]
