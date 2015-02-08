# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150208_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='current_location',
            field=models.OneToOneField(blank=True, to='api.Location', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='is_publishing',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
