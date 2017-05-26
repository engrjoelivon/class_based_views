# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_id', models.IntegerField()),
                ('task_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Record name',
            },
            bases=(models.Model,),
        ),
    ]
