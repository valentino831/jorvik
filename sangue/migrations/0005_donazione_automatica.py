# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-13 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sangue', '0005_auto_20160906_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='donazione',
            name='automatica',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Automatica'),
        ),
    ]
