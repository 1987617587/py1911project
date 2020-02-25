from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import login as lin, authenticate, logout as lout
from django.db.models import Max,Sum,Min,Avg
from qikuapp.forms import CommentForm
from .models import *
# 分页和分页器
from django.core.paginator import Page, Paginator


def index(request):
    # 未登录展示部分功能，诱导游客登录 登陆后跳转list页面展示全部数据
    # return HttpResponse("首页")
    ads = Ads.objects.all()

    teachers = Teacher.objects.all()
    curriculum = Curriculum.objects.all()
    categories = Category.objects.all()
    print(request.user)
    return render(request, 'index.html', locals())


def contact(request):
    # return HttpResponse("联系我们")
    return render(request, 'base.html')



def login(request):
    if request.method == "GET":
        return render(request, '登录.html', locals())
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            # user = User.objects.get(username=username)
            print("找到用户", user)
            print(user.username)
            print(user.password)
            # 验证成功生成cookie
            lin(request, user)
            # 人性化处理、
            next_url = request.GET.get("next")
            if next_url:
                url = next_url
            else:
                url = reverse("qikuapp:list")
            return redirect(to=url)
            # return render(request, '培训信息.html', locals())
        except:
            print("未找到相应用户，登录失败")
            error = "用户名或密码错误,登录失败"
            return render(request, '登录.html', locals())


def register(request):
    if request.method == "GET":
        return render(request, '注册.html', locals())
    elif request.method == "POST":
        print(request.POST.get('telephone'))
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if telephone and password and repassword:
            if password != repassword:
                # return HttpResponse("密码不一致")
                error = "两次密码输入不一致"
                return render(request, '注册.html', locals())
            else:
                User.objects.create_user(username=telephone, password=password)
                return render(request, '登录.html')
        error = "必须输入手机号（用户名）、邮箱和密码"
        return render(request, '注册.html', locals())


def loginout(request):
    # 删除 cookie

    lout(request)
    url = reverse("qikuapp:index")

    return redirect(to=url)
    # return HttpResponse("退出")


def list(request):
    if request.user and request.user.username != '':
        print(request.user)
        print(request.user.username)

        # 登陆后展示全部数据
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
    else:
        # 使用拼接，人性化处理，传递未登录之前准备进入的页面
        url = reverse("qikuapp:index")
        return redirect(to=url)


def detail(request, c_id):
    # ads2 = Ads2.objects.all()
    # curriculum = Curriculum.objects.get(id=c_id)
    #
    # return render(request, '购买页面.html', locals())
    if request.user and request.user.username != '':
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
    else:
        url = reverse('qikuapp:login')+'?next=/detail/'+c_id+'/'
        return redirect(to=url)


def buy(request,c_id):
    # 购物车
    user = request.user
    try:
        curriculum = Curriculum.objects.get(id=c_id)
        # 关联用户和课程
        request.user.curriculum.add(curriculum)
    except:
        error = "加入购物车失败"
    # curriculum = request.user.curriculum
    money = request.user.curriculum.all().aggregate(Sum('price')).get("price__sum")
    if not money:
        money = 0
    money_to_integral = money*0.1
    return render(request, '提交订单.html', locals())


def add(request, c_id):
    # 加入购物车，创建用户与课程直接的关系
    user = request.user
    try:
        curriculum = Curriculum.objects.get(id=c_id)
        # 关联用户和课程
        request.user.curriculum.add(curriculum)
    except:
        error = "加入购物车失败"
    url = reverse("qikuapp:list")
    return redirect(to=url)


def favicon(request):
    return redirect(to="/static/favicon.ico")
