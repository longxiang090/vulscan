# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-09 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('aizhan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='spider_conf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('exec_sousuo', models.CharField(blank=True, max_length=255, null=True)),
                ('page_sousuo', models.IntegerField(default=100)),
                ('quanzhong_vaule', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='zoomeye_host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('hostname', models.CharField(blank=True, max_length=255, null=True)),
                ('port', models.CharField(blank=True, max_length=255, null=True)),
                ('os_version', models.CharField(blank=True, max_length=255, null=True)),
                ('device', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='zoomeye_web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('server', models.CharField(blank=True, max_length=255, null=True)),
                ('db', models.CharField(blank=True, max_length=255, null=True)),
                ('webapp', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
