# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FOadmin', '0004_profile_fo_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fo_user_birthday',
            field=models.DateField(null=True, verbose_name='День рождения'),
        ),
    ]