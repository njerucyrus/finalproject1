# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-25 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_seller_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='user',
            new_name='seller_username',
        ),
    ]
