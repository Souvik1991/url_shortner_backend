# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-06-06 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original_url', models.TextField()),
            ],
            options={
                'db_table': 'urls',
            },
        ),
    ]
