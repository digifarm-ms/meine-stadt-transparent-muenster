# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0009_auto_20180216_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='oparl_access_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='oparl_download_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfile',
            name='oparl_access_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfile',
            name='oparl_download_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
