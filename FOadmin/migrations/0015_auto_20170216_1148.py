# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 06:48
from __future__ import unicode_literals

import FOadmin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FOadmin', '0014_profile_fo_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fo_user_photo',
            field=models.ImageField(blank=True, upload_to=FOadmin.models.fo_user_upload_path),
        ),
    ]