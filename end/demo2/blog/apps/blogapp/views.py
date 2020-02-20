from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # return HttpResponse("首页")
    return render(request, 'index.html')



def detail(request, articleid):
    # return HttpResponse("详情")
    return render(request, 'single.html')



def contact(request):
    # return HttpResponse("联系我们")
    return render(request, 'contact.html')

