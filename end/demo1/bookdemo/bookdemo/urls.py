"""bookdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# 路由（网址） 每一个网站均需要绑定视图函数 视图函数给予页面返回
# MVT   V视图函数 3个作用 1.接受数据2.数据处理3.返回响应
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("这里是首页")
#
#
# def list(request):
#     return HttpResponse("这里是列表页")
#
#
# def json_data(request):
#     return HttpResponse("{'name':'zzy','age':'20'}")


urlpatterns = [
    path('admin/', admin.site.urls),
    # # 将admin路由和index视图函数绑定
    # path('index/', index,),
    # # 将list路由和list视图函数绑定
    # path('list/', list,),
    # path('json/', json_data,),
    # 多个应用 为了方便管理 1.使用path将booktest的路由 进行包含
    # path('booktest/',include('booktest.urls',)),
    # 优化 因为只有一个应用 可以省略booktest/
    path('',include('booktest.urls',namespace='booktest')),

]

# 项目的所有路由地址配置文件
# admin路由是django自带的后台管理路由

# 总的路由匹配文件 == 项目路由文件  使用include包含应用路由文件