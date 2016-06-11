# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20160605_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='predmet',
            name='studenti',
            field=models.ManyToManyField(through='student.Ocena', to='student.Student'),
        ),
        migrations.AlterField(
            model_name='predmet',
            name='nazivPredmeta',
            field=models.CharField(max_length=50, verbose_name='Naziv predmeta'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentIme',
            field=models.CharField(max_length=15, verbose_name='Ime'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentPrezime',
            field=models.CharField(max_length=30, verbose_name='Prezime'),
        ),
    ]
