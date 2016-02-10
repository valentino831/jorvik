# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0031_auto_20160203_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estensione',
            name='appartenenza',
            field=models.ForeignKey(null=True, to='anagrafica.Appartenenza', related_name='estensioni', blank=True),
        ),
    ]
