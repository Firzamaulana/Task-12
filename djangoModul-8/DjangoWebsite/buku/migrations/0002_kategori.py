# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2023-05-13 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=100)),
            ],
        ),
    ]
