# 引入路由绑定函数
from django.conf.urls import url

from . import views
#
# 2.每一个路由文件中 必须编写路由数组
urlpatterns = [
    url(r'^index/$', views.index),
    # 第一个参数就是路由 第二个是视图函数
    url(r'^list/$',views.list),
    url(r'^about/$',views.about),
    # 使用正则分组 (\d+) 将正则分组匹配到的内容作为实参传递给视图函数
    url(r'detail/(\d+)/',views.detail),
    # url(r'^detail/([0-9]+)/$', views.detail),
]
