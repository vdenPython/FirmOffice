# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegalEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fo_short_title', models.CharField(max_length=100, verbose_name='Краткое наименование')),
            ],
            options={
                'verbose_name_plural': 'Юридические лица',
                'verbose_name': 'Юридическое лицо',
            },
        ),
    ]
