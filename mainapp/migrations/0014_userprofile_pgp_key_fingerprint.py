# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0013_auto_20181005_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pgp_key_fingerprint',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
