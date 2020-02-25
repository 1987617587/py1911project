from django.conf.urls import url,include
from django.views.generic.base import RedirectView
from . import views

app_name = 'qikuapp'

urlpatterns = [
    # url(r'^index/$',views.index,name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^loginout/$', views.loginout, name='loginout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^list/$', views.list, name='list'),
    url(r'^buy/(\d+)/$', views.buy, name='buy'),
    url(r'^add/(\d+)/$', views.add, name='add'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^favicon.ico$', views.favicon, name='favicon'),
    url(r'^search/', include('haystack.urls')),
# url(r'^rss/$', ArticleFeed(),name='rss'),
]
