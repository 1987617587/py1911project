from django.shortcuts import render

# Create your views here.


# MVT V视图模块
# 在此处接受请求 处理数据 返回响应
from django.http import HttpResponse
# 3.在views.py中编写视图函数
def index(request):
    return HttpResponse("这里是首页")


def list(request):
    return HttpResponse("这里是列表页")


def about(request):
    return HttpResponse("这里是关于页")