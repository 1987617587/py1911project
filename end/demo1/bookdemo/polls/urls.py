from django.conf.urls import url

from . import views
# 应用名
app_name = "polls"

urlpatterns = [
    url(r'^$', views.index,name="index"),
    # 首页优化 http://127.0.0.1:8000/ 直接进入首页
    # url(r'^$', views.index,name='index'),
    # # 第一个参数就是路由 第二个是视图函数
    # url(r'^list/$',views.list,name='list'),
    # url(r'^about/$',views.about,name='about'),
    # # 以^开始，以$结束 更加严谨
    # # 使用正则分组 (\d+) 将正则分组匹配到的内容作为实参传递给视图函数
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    # # url(r'^detail/([0-9]+)/$', views.detail),
    #
    # # 删除功能
    # url(r'^delbook/(\d+)/$', views.delbook, name='delbook'),
    # url(r'^delhero/(\d+)/$', views.delhero, name='delhero'),
    # # 添加英雄
    # url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    # url(r'^addbook/$', views.addbook, name='addbook'),
    # # 编辑英雄
    # url(r'^vote/(\d+)/$', views.vote, name='vote'),
    url(r'^votenums/(\d+)/$', views.votenums, name='votenums'),
    # url(r'^editbook/(\d+)/$', views.editbook, name='editbook'),

]