# Generated by Django 2.0.7 on 2018-07-31 12:12

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180727_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
    ]
