from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
app_name = 'qikuapp'

urlpatterns = [
    # url(r'^index/$',views.index,name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^list$', views.list, name='list'),
    url(r'^buy$', views.buy, name='buy'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^favicon.ico$', views.favicon,name='favicon'),
    # url(r'^rss/$', ArticleFeed(),name='rss'),
]
