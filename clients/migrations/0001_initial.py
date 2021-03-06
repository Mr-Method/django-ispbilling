# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-13 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Shop_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1500)),
                ('address', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField()),
                ('other_details', models.CharField(max_length=100, null='true')),
            ],
        ),
        migrations.AddField(
            model_name='shop_category',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Shop_Type'),
        ),
        migrations.AddField(
            model_name='shop_category',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Shops'),
        ),
    ]
