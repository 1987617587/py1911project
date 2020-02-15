from django.contrib import admin

# Register your models here.
# django自带的后台管理操作需要在此处实现

# 注册自己需要管理的模型 Book Hero
from .models import Book,Hero,User


from django.contrib import admin
from django.contrib.admin import ModelAdmin


class HeroInline(admin.StackedInline):
    """
    定义关联类

    """
    model = Hero
    extra = 1


class HeroAdmin(ModelAdmin):
    """
    定义模型管理类
    通过该类可以修改后台页面
    """
    # 更改后端显示列
    list_display = ('name', 'gender', 'book')
    # 每页显示一个 分页会出现在下侧
    list_per_page = 5
    # 定义搜索字段 （包含标题 价格） 搜索框会出现在上侧
    search_fields = ('name', 'gender')
    # 指定过滤字段 过滤框会出现在右侧
    list_filter = ('name', 'gender', 'book')


class BookAdmin(ModelAdmin):
    """
    定义模型管理类
    通过该类可以修改后台页面
    """
    # 更改后端显示列
    list_display = ('title','price','pub_date','author')
    # 每页显示一个
    list_per_page = 10
    # 定义搜索字段 （包含标题 价格）
    search_fields = ('title','price','author')
    # 指定过滤字段
    list_filter = ('title','price','pub_date','author')

    # 通过指定关联类进行关联
    inlines = [HeroInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(User)