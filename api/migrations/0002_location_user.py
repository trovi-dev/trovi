# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(to='api.User', default=1),
            preserve_default=False,
        ),
    ]
