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

    return render(request, 'base.html', locals())


def contact(request):
    return HttpResponse("联系我们")


def detail(request, c_id):

    # return HttpResponse("详情")
    return render(request, '综合信息页面.html', locals())

def favicon(request):
    return redirect(to="/static/favicon.ico")
