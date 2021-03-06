# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FOadmin', '0010_profile_fo_right_create_working_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fo_right_invite_any_user_workgroup',
            field=models.BooleanField(default=False, verbose_name='Пригласить любого пользователя в рабочую группу'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fo_right_create_working_group',
            field=models.BooleanField(default=False, verbose_name='Создание рабочей группы'),
        ),
    ]
