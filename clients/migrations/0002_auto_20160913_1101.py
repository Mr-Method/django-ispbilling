# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-13 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Customer first name. Example : Porimol', max_length=20)),
                ('last_name', models.CharField(help_text='Customer last name. Example : Chandro', max_length=20, null=True)),
                ('nid_number', models.CharField(help_text='Customer national ID number.', max_length=60, null=True)),
                ('mobile_number', models.CharField(help_text='01700000000', max_length=15, null=True)),
                ('email_address', models.EmailField(help_text='Example : email@yourdomain.com', max_length=254, null=True)),
                ('present_address', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='shop_category',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='shop_category',
            name='shop_id',
        ),
        migrations.DeleteModel(
            name='Shop_Category',
        ),
        migrations.DeleteModel(
            name='Shop_Type',
        ),
        migrations.DeleteModel(
            name='Shops',
        ),
    ]
