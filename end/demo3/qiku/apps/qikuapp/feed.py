# 添加RSS订阅功能
# 使用Django框架集成的RSS包装工具
from django.contrib.syndication.views import Feed
from django.shortcuts import reverse

from qikuapp.models import Curriculum


class CurriculumFeed(Feed):
    title = "在线学习全栈技术"
    description = "定期线上教学"
    link = "/"

    def items(self):
        return Curriculum.objects.all().order_by("-create_time")[:3]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.teacher

    def item_link(self, item):
        url = reverse("qikuapp:detail", args=(item.id,))
        return url
        # return "/detail/"+item.id+'/'
