# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('difficulty_rating', models.IntegerField()),
                ('difficulty_rating_old', models.IntegerField(null=True)),
                ('step_count', models.IntegerField()),
                ('freeze_count', models.IntegerField(default=0)),
                ('shock_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'80')),
                ('code', models.CharField(max_length=b'1')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'5')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'200')),
                ('name_translation', models.CharField(max_length=b'200', null=True)),
                ('artist', models.CharField(max_length=b'200')),
                ('artist_translation', models.CharField(max_length=b'200', null=True)),
                ('bpm', models.IntegerField()),
                ('bpm_max', models.IntegerField(null=True)),
                ('genre', models.CharField(max_length=b'200', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='chart',
            name='difficulty',
            field=models.ForeignKey(to='tracker.Difficulty'),
        ),
        migrations.AddField(
            model_name='chart',
            name='song',
            field=models.ForeignKey(to='tracker.Song'),
        ),
        migrations.AddField(
            model_name='chart',
            name='style',
            field=models.ForeignKey(to='tracker.Style'),
        ),
    ]
