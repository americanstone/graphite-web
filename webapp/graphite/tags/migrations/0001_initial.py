# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-07-07 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeriesTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='seriestag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.Tag'),
        ),
        migrations.AddField(
            model_name='seriestag',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.TagValue'),
        ),
        migrations.AlterUniqueTogether(
            name='seriestag',
            unique_together=set([('series', 'tag')]),
        ),
    ]
