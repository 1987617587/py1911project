from django.template import Library
from ..models import *

# 编译过滤器
register = Library()


# 使用装饰器装饰标签
@register.filter
def date_format(date):
    return "%d-%d-%d" % (date.year, date.month, date.day)


@register.filter
def author_format(author, info):
    return info + ":" + author.upper()


@register.simple_tag
def get_stars_teachers(num=5):
    return Teacher.objects.filter(stars=num)


@register.simple_tag
def get_latest_curriculum(num=4):
    return Curriculum.objects.all().order_by("-create_time")[:num]


@register.simple_tag
def get_latest_curriculum_price():
    return Curriculum.objects.all().order_by("price")[::]

@register.simple_tag
def get_hot_curriculum(num=1):
    return Curriculum.objects.all().order_by("price")[:num]


@register.simple_tag
def get_free_curriculum(num=1):
    return Curriculum.objects.all().order_by("-price")[:num]
#
# @register.simple_tag
# def get_latest_dates(num=3):
#     return Article.objects.dates("create_time", 'month', "DESC")[:num]
#
#
# @register.simple_tag
# def get_categorys():
#     return Category.objects.all().order_by("id")[::]
#
#
#
# @register.simple_tag
# def get_tags():
#     return Tag.objects.all().order_by("id")[::]
