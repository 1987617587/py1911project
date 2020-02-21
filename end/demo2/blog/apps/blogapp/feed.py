# 添加RSS订阅功能
# 使用Django框架集成的RSS包装工具
from django.contrib.syndication.views import Feed
from django.shortcuts import reverse

from blogapp.models import Article


class ArticleFeed(Feed):
    title = "web全栈开发技术"
    description = "定期发布一些技术文章"
    link = "/"

    def items(self):
        return Article.objects.all().order_by("-create_time")[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.auther

    def item_link(self, item):
        url = reverse("blogapp:detail", args=(item.id,))
        return url
        # return "/detail/"+item.id+'/'
