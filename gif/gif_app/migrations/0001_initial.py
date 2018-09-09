# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=7, choices=[(b'OK', b'OK'), (b'notOK', b'notOK'), (b'ongoing', b'ongoing')])),
                ('active', models.BooleanField()),
                ('path', models.ImageField(upload_to=b'gif/static/img/')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField(default=1)),
            ],
        ),
    ]
