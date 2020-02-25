# 创建索引类
from haystack import indexes
from .models import Curriculum


# 1.类名必须为 模型名Index
# 2.get_model 必须返回模型
class CurriculumIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Curriculum

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
