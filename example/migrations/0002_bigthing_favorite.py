# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigthing',
            name='favorite',
            field=models.OneToOneField(related_name='favorite_of', default=1, to='example.ChildThing'),
            preserve_default=False,
        ),
    ]
