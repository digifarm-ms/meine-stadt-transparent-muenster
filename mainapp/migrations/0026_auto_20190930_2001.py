# Generated by Django 2.1.12 on 2019-09-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0025_auto_20190917_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallocation',
            name='search_str',
            field=models.CharField(blank=True, db_index=True, max_length=767, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='search_str',
            field=models.CharField(blank=True, max_length=767, null=True, unique=True),
        ),
    ]
