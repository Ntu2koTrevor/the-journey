# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('blog', '0006_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('message', models.CharField(max_length=200)),
                ('message_pt', models.CharField(max_length=200, null=True)),
                ('message_es', models.CharField(max_length=200, null=True)),
                ('message_fr', models.CharField(max_length=200, null=True)),
                ('language', models.CharField(blank=True, choices=[('pt', 'Português'), ('es', 'Espanhol'), ('fr', 'Francês')], max_length=6, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
