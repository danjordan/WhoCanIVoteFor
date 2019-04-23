# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-19 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("people", "0018_auto_20170518_1255")]

    operations = [
        migrations.CreateModel(
            name="CV",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(blank=True, null=True)),
                ("thumb_url", models.URLField(blank=True, null=True)),
                ("last_modified", models.DateTimeField(blank=True, null=True)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="people.Person",
                    ),
                ),
            ],
        )
    ]
