# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-13 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0011_auto_20160612_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]