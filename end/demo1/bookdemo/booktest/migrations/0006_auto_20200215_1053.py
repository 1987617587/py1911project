# Generated by Django 3.0.3 on 2020-02-15 02:53

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]
