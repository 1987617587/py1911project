# Generated by Django 3.0.3 on 2020-02-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qikuapp', '0002_auto_20200224_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ads', verbose_name='图片')),
                ('desc', models.CharField(blank=True, max_length=20, null=True, verbose_name='图片说明')),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=20, verbose_name='教师名'),
        ),
    ]