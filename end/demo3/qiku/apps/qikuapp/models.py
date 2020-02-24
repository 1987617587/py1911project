from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField


class Ads(models.Model):
    img = models.ImageField(upload_to="ads", verbose_name="图片")
    desc = models.CharField(max_length=20, null=True, blank=True, verbose_name="图片说明")

    class Mate:
        verbose_name = "图片表"


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = "分类表"


class Curriculum(models.Model):
    name = models.CharField(max_length=20, verbose_name="教师姓名")
    category = models.ManyToManyField(Category, verbose_name="授课分类")
    price = models.PositiveIntegerField(default=1000, verbose_name="课程费用")
    days = models.PositiveIntegerField(default=7, verbose_name="课程时长")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="开课时间")
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name="授课教师")

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = "课程表"


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name="课程名")

    field = models.CharField(max_length=50, verbose_name="权威领域")
    # body = models.TextField(verbose_name="正文")
    # 使用富文本字段类型
    introduce = UEditorField(imagePath="imgs/", width="100%", verbose_name="简介")
    stars = models.PositiveIntegerField(default=3, verbose_name="评价星级")

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = "教师表"


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="评论人")
    url = models.URLField(default="http://www.zzy.com", verbose_name="个人主页")
    email = models.EmailField(default="1862655@qq.com", verbose_name="个人邮箱")
    body = models.TextField(verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, verbose_name="所属课程")

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = "评论表"
