# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-28 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('declaracion', '0006_auto_20190828_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaracion',
            name='plantilla',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='declaracion.Plantilla'),
        ),
    ]
