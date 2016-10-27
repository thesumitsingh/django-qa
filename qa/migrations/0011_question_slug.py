# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-27 15:53
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify


def gen_slug(apps, schema_editor):
    MyModel = apps.get_model('qa', 'Question')
    for row in MyModel.objects.all():
        row.slug = slugify(row.title)
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0010_auto_20160919_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.RunPython(
            gen_slug, reverse_code=migrations.RunPython.noop),
    ]