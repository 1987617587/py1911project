# Generated by Django 3.0.3 on 2020-02-24 09:43

import DjangoUeditor.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ads', verbose_name='图片')),
                ('desc', models.CharField(blank=True, max_length=20, null=True, verbose_name='图片说明')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='课程名')),
                ('field', models.CharField(max_length=50, verbose_name='权威领域')),
                ('introduce', DjangoUeditor.models.UEditorField(verbose_name='简介')),
                ('stars', models.PositiveIntegerField(default=3, verbose_name='评价星级')),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='课程名')),
                ('introduce', models.CharField(max_length=120, verbose_name='课程介绍')),
                ('img', models.ImageField(upload_to='imgs', verbose_name='课程图片')),
                ('price', models.PositiveIntegerField(default=1000, verbose_name='课程费用')),
                ('days', models.PositiveIntegerField(default=7, verbose_name='课程时长')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='开课时间')),
                ('category', models.ManyToManyField(to='qikuapp.Category', verbose_name='授课分类')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qikuapp.Teacher', verbose_name='授课教师')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='评论人')),
                ('url', models.URLField(default='http://www.zzy.com', verbose_name='个人主页')),
                ('email', models.EmailField(default='1862655@qq.com', max_length=254, verbose_name='个人邮箱')),
                ('body', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qikuapp.Curriculum', verbose_name='所属课程')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='qikuapp.Curriculum')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
