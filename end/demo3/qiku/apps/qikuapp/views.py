from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from qikuapp.forms import CommentForm
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


def register(request):
    return render(request, '注册.html', locals())


def list(request):
    ads2 = Ads2.objects.all()
    type_page = request.GET.get("type")
    category_id, teacher_id, price_id = None, None, None
    if type_page == "category":
        category_id = request.GET.get("category_id")
        try:
            category = Category.objects.get(id=category_id)
            curriculum = category.curriculum_set.all()
        except:
            return HttpResponse("标签不合法！")
    elif type_page == "teacher":
        teacher_id = request.GET.get("teacher_id")
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            curriculum = teacher.curriculum_set.all()
        except:
            return HttpResponse("标签不合法！")
    elif type_page == "price":
        curriculum_price = request.GET.get("curriculum_price")

        curriculum = Curriculum.objects.filter(price=curriculum_price)

    else:
        curriculum = Curriculum.objects.all()
    teachers = Teacher.objects.all()

    categories = Category.objects.all()
    # 分页器
    paginator = Paginator(curriculum, 2)
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request, '培训信息.html', locals())


def detail(request, c_id):
    # ads2 = Ads2.objects.all()
    # curriculum = Curriculum.objects.get(id=c_id)
    #
    # return render(request, '购买页面.html', locals())
    if request.method == "GET":
        try:
            ads2 = Ads2.objects.all()
            curriculum = Curriculum.objects.get(id=c_id)
            cf = CommentForm()
            return render(request, '购买页面.html', locals())
        except:
            return HttpResponse("查询无果")
    else:
        cf = CommentForm(request.POST)
        if cf.is_valid():
            # 此时cf是一个表单，不是实例
            # cf.article = Article.objects.get(id=articleid)
            # 保存前对commit默认值修改为False  comment就是实例了
            comment = cf.save(commit=False)
            comment.curriculum = Curriculum.objects.get(id=c_id)
            comment.save()

            url = reverse("qikuapp:detail", args=(c_id,))
            return redirect(to=url)

        else:
            ads2 = Ads2.objects.all()
            curriculum = Curriculum.objects.get(id=c_id)
            cf = CommentForm()
            errors = "输入格式有误！"
            return render(request, '购买页面.html', locals())


def buy(request):
    # 购物车

    return render(request, '提交订单.html', locals())


def favicon(request):
    return redirect(to="/static/favicon.ico")
