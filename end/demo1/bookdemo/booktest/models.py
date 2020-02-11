from django.db import models

# Create your models here.


# MVT M数据模型
# ORM M数据模型
# 在此处进行编写数据模型类
# 每一张表就是一个模型类
# 有了ORM之后我们就可以定义出表对应的模型类
#通过操作模型去操作数据库 不需要写SQL语句


# 有了模型类 如何与数据库交互
# 1.注册模型在settingg.py中的INSTALLED_APPS添加应用名
# 2.生成迁移文件 用于数据库交互 python mange.py makemigrations
#    会在对应的应用下方生成迁移文件 不需要关注
# 3.执行迁移 会在对应的数据库中生成对应的表 python manage.py migrate
# 模型类更改之后 需要再次生成迁移文件 执行迁移 即重复2，3
class Book(models.Model):
    """
    Book继承了Model类 因为Model可以操作数据库
    """
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1989-06-01")
    price = models.FloatField(default=0)
    # def __str__(self):
    #     return f"{self.pk}"


class Hero(models.Model):
    """
    Hero继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='male')
    content = models.CharField(max_length=100)
    # book 是一对多中的外键 on_delet 代表删除主表数据时如何做
    book = models.ForeignKey('Book',on_delete=models.CASCADE)




































