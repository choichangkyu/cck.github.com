# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wPlayGame', '0002_auto_20160415_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='comment',
            name='password',
            field=models.CharField(default=b'1111', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(default=b'1111', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
