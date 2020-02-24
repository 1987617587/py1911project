from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from .models import *
# 分页和分页器
from django.core.paginator import Page, Paginator


def index(request):
    # return HttpResponse("首页")
    ads = Ads.objects.all()

    teachers = Teacher.objects.all()
    curriculum = Curriculum.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', locals())


def contact(request):
    return HttpResponse("联系我们")


def login(request):
    return render(request, '登录.html', locals())


def list(request):
    ads2 = Ads2.objects.all()
    type_page = request.GET.get("type")
    if type_page == "category":
        pass
    else:
        pass
    teachers = Teacher.objects.all()
    curriculum = Curriculum.objects.all()
    categories = Category.objects.all()
    # 分页器
    paginator = Paginator(curriculum, 2)
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request, '培训信息.html', locals())


def detail(request, c_id):
    ads2 = Ads2.objects.all()
    curriculum = Curriculum.objects.get(id=c_id)

    return render(request, '购买页面.html', locals())


def buy(request):
    # 购物车
    ads2 = Ads2.objects.all()

    return render(request, '提交订单.html', locals())


def favicon(request):
    return redirect(to="/static/favicon.ico")
