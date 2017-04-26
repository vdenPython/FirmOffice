# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 05:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FOadmin', '0014_workinggrouppartner_fo_right_invite_group'),
        ('FoBusinessProcess', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessprocessadmin',
            name='businessprocess_ptr',
        ),
        migrations.AlterModelOptions(
            name='businessprocess',
            options={'verbose_name': 'Бизнес процесс', 'verbose_name_plural': 'Бизнес процессы'},
        ),
        migrations.AlterModelOptions(
            name='lineofbusiness',
            options={'verbose_name': 'Отрасль производства (линия бизнеса)', 'verbose_name_plural': 'Отрасль производства (линия бизнеса)'},
        ),
        migrations.AddField(
            model_name='businessprocess',
            name='fo_business_process_manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.ProtectedError, to='FOadmin.Profile', verbose_name='Руководитель Бизнесс процесса'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BusinessProcessAdmin',
        ),
    ]