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
    # if request

    # pass
