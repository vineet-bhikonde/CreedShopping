# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='product_id',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='pro_id',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
