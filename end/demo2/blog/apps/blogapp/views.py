from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# 分页和分页器
from django.core.paginator import Page, Paginator


# Create your views here.

def index(request):
    # return HttpResponse("首页")
    ads = Ads.objects.all()
    type_page = request.GET.get("type")
    year,month = None,None
    if type_page == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        articles = Article.objects.filter(create_time__year=year, create_time__month=month).order_by("-create_time")
    else:
        articles = Article.objects.all()

    # locals()可以返回作用域 局部变量
    # print(locals())
    # return render(request, 'index.html',locals())
    # 添加分页
    paginator = Paginator(articles, 2)
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request, 'index.html', {"ads": ads, "page": page,'type':type_page,"year":year,"month":month})


def detail(request, articleid):
    # return HttpResponse("详情")
    return render(request, 'single.html')


def contact(request):
    # return HttpResponse("联系我们")
    return render(request, 'contact.html')


def favicon(request):
    return redirect(to="/static/favicon.ico")
