# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_location_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalizedLocation',
            fields=[
                ('location_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='api.Location', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.location',),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('unique_identifier', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='normalizedlocation',
            name='venue',
            field=models.ForeignKey(to='api.Venue'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='location',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longitude',
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(max_length=255, default='My House'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, default='Point (0 0)'),
            preserve_default=False,
        ),
    ]
