# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 21:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("hustings", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="husting", options={"ordering": ["-starts"]}
        )
    ]
