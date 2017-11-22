# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cartitems_pro_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='pro_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]