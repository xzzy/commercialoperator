# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-04-21 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0041_auto_20200418_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalPreEventsParks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities', models.CharField(blank=True, max_length=255, null=True)),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_event_proposal', to='commercialoperator.Park')),
                ('proposal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_event_parks', to='commercialoperator.Proposal')),
            ],
        ),
    ]