from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import Book,Hero
# Create your views here.


# MVT V视图模块
# 在此处接受请求 处理数据 返回响应
from django.http import HttpResponse,HttpResponseRedirect
# 3.在views.py中编写视图函数
def index(request):

    # # return HttpResponse("这里是<h1>首页</h1>")
    # # 1.获取模板
    # template = loader.get_template('index.html')
    # # 2.渲染模板数据
    # books = Book.objects.all()
    # context = {'books':books}
    # result = template.render(context)
    # # 3.将渲染结果使用httpresponse返回
    # return HttpResponse(result)

    # 快捷方式 (将上面3步简化操作)
    books = Book.objects.all()
    return render(request,'index.html',{'books':books})

def list(request):
    return HttpResponse("这里是列表页")


def detail(request,b_id):
    # # return HttpResponse(f"这里{b_id}书是详情页")
    # # 1.获取模板
    # template = loader.get_template('detail.html')
    # # 2.渲染模板数据
    # book = Book.objects.get(id = b_id)
    # context = {'book': book}
    # result = template.render(context)
    # # 3.将渲染结果使用httpresponse返回
    # return HttpResponse(result)

    # 快捷方式 (将上面3步简化操作)
    book = Book.objects.get(id = b_id)
    return render(request,'detail.html',{'book':book})

def about(request):
    return HttpResponse("这里是关于页")


def delbook(request,bookid):
    book = Book.objects.get(id = bookid)
    book.delete()
    # return HttpResponse("删除成功")
    # return HttpResponseRedirect(redirect_to='/booktest/'+bookid)
    # return HttpResponseRedirect(redirect_to='/')
    # return redirect(to='/')

    # 在
    url = reverse('booktest:index')
    return redirect(to=url)


def delhero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    # 一定要先获取在删除
    bookid = hero.book.id
    hero.delete()
    url = reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)

def addhero(request,bookid):
    print(bookid)
    if request.method == 'GET':
        return render(request,'addhero.html')
    elif request.method == 'POST':
        h = Hero()
        h.name =request.POST.get("heroname")
        print(h.name)
        h.gender =request.POST.get("sex")
        # h.gender = True
        h.content = request.POST.get("content")
        h.book = Book.objects.get(id = bookid)
        h.save()
        url = reverse("booktest:detail", args=(bookid,))
        return redirect(to=url)

def addbook(request):
    if request.method == 'GET':
        return render(request,'addbook.html')
    elif request.method == 'POST':
        b = Book()
        b.title =request.POST.get("title")
        print(b.title)
        b.price =request.POST.get("price")
        # h.gender = True
        b.pub_date = request.POST.get("pub_date")

        b.save()
        url = reverse("booktest:index")
        return redirect(to=url)


def edithero(request,heroid):
    hero = Hero.objects.get(id = heroid)
    print(hero)
    # 使用get方法进入英雄的编辑页面
    if request.method == 'GET':
        return render(request,"edithero.html",{'hero':hero})
    elif request.method == 'POST':
        hero.name = request.POST.get("heroname")
        hero.gender = request.POST.get("sex")
        hero.content = request.POST.get("content")
        hero.save()
        # 注意数组类型 不加，会报类型错误的
        url = reverse('booktest:detail',args=(hero.book.id,))
        return redirect(to=url)


def editbook(request,bookid):
    book = Book.objects.get(id = bookid)
    print(book)
    print(book.pub_date)
    book.pub_date = str(book.pub_date)
    print(type(book.pub_date))
    # 使用get方法进入英雄的编辑页面
    if request.method == 'GET':
        return render(request,"editbook.html",{'book':book})
    elif request.method == 'POST':
        book.name = request.POST.get("title")
        book.price = request.POST.get("price")
        book.pub_date = request.POST.get("pub_date")
        book.save()
        # 注意数组类型 不加，会报类型错误的
        url = reverse('booktest:index')
        return redirect(to=url)