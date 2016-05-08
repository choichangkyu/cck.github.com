# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('wPlayGame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=' ', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=b'/Users/cck/Documents/firstproject/blog/static/upload/sheep.jpg', upload_to=b'/Users/cck/Documents/firstproject/blog/static/upload/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=50),
        ),
    ]
