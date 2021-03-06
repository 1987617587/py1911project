# Generated by Django 3.0.3 on 2020-02-21 11:19

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='imgs',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=DjangoUeditor.models.UEditorField(verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blogapp.Tag', verbose_name='标签'),
        ),
    ]
