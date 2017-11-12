# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 15:28
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloorPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('floor', models.SmallIntegerField(verbose_name='floor')),
                ('image', models.ImageField(help_text='floor plan image', upload_to='', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=75, verbose_name='name')),
                ('address', models.CharField(blank=True, db_index=True, max_length=256, verbose_name='address')),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326, verbose_name='geometry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ObjectLocation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('object_id', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('outdoor', 'Outdoor'), ('indoor', 'Indoor'), ('mobile', 'Mobile')], max_length=8)),
                ('indoor', models.CharField(blank=True, max_length=64, null=True, verbose_name='indoor position')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('floorplan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_loci.FloorPlan')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_loci.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='floorplan',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_loci.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='floorplan',
            unique_together=set([('location', 'floor')]),
        ),
    ]
