# Generated by Django 4.1 on 2022-08-06 20:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('ogc_fid', models.AutoField(primary_key=True, serialize=False)),
                ('idx', models.FloatField(blank=True, null=True)),
                ('task_id', models.CharField(blank=True, max_length=255, null=True)),
                ('number_0_count', models.FloatField(blank=True, db_column='0_count', null=True)),
                ('number_1_count', models.FloatField(blank=True, db_column='1_count', null=True)),
                ('number_2_count', models.FloatField(blank=True, db_column='2_count', null=True)),
                ('number_3_count', models.FloatField(blank=True, db_column='3_count', null=True)),
                ('total_count', models.FloatField(blank=True, null=True)),
                ('number_0_share', models.FloatField(blank=True, db_column='0_share', null=True)),
                ('number_1_share', models.FloatField(blank=True, db_column='1_share', null=True)),
                ('number_2_share', models.FloatField(blank=True, db_column='2_share', null=True)),
                ('number_3_share', models.FloatField(blank=True, db_column='3_share', null=True)),
                ('agreement', models.FloatField(blank=True, null=True)),
                ('unnamed_0', models.FloatField(blank=True, db_column='unnamed: 0', null=True)),
                ('changesetid', models.FloatField(blank=True, null=True)),
                ('lastedit', models.DateTimeField(blank=True, null=True)),
                ('osmid', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.FloatField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('editor', models.CharField(blank=True, max_length=255, null=True)),
                ('userid', models.FloatField(blank=True, null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'building',
                'managed': True,
            },
        ),
    ]