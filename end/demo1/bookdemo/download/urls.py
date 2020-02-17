from django.conf.urls import url
from . import views
from django.http import FileResponse

# 应用名
app_name = "download"


def load(resquest, filename):
    # return FileResponse(open("1.txt","rb"),filename="python.txt",as_attachment=True)
    return FileResponse(open(filename, "rb"), content_type='application/msword', filename=filename, as_attachment=True)
    # return FileResponse(open(filename+'.txt', "rb"), content_type='application/msword', filename=filename+'txt', as_attachment=True)


urlpatterns = [
    # url(r'^(\w+)$',load)
    # url(r'^(\d+)$',load)
    # url(r"^download/$",views.download,name="download"),

    url(r'^(.*?)/$', load)

]
