# 引入路由绑定函数
from django.conf.urls import url

from . import views
#
# 2.每一个路由文件中 必须编写路由数组
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^list/$',views.list),
    url(r'^about/$',views.about),
    # url(r'^detail/([0-9]+)/$', views.detail),
]
