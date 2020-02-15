from django.db import models


# Create your models here.


# MVT M数据模型
# ORM M数据模型
# 在此处进行编写数据模型类
# 每一张表就是一个模型类
# 有了ORM之后我们就可以定义出表对应的模型类
# 通过操作模型去操作数据库 不需要写SQL语句


# 有了模型类 如何与数据库交互
# 1.注册模型在settingg.py中的INSTALLED_APPS添加应用名
# 2.生成迁移文件 用于数据库交互 python manage.py makemigrations
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
    # 添加一列 因为已经不为空，需要添加默认值

    author = models.CharField(max_length=20, default='金庸')

    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    Hero继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    # book 是一对多中的外键 on_delet 代表删除主表数据时如何做
    # 在定义关系字段时 使用related_name="heros" 则一找多 一方对象.heros.all() == 一方对象.小写多方类名_set.all()
    # 注意 一旦添加related_name="heros" 不能再使用 一方对象.小写多方类名_set.all()
    book = models.ForeignKey('Book', on_delete=models.CASCADE,related_name="heros")

    def __str__(self):
        return self.name


# django ORM关联查询
# 多方Hero 一方 Book
# 1.多找一 ,多方对象.关系字段  exp:h1.book.title
# 2.一找多， 一方对象.小写多方类名_set.all()  exp: b1.hero_set.all()


class UserManager(models.Manager):
    """
    自定义模型管理类 该模型不再具有objects对象 self就是objects对象
    """

    def deleteByTelePhone(self, tele):
        # django 默认的objects是Manager类型 此时self 就是 objects对象
        user = self.get(telephone=tele)
        user.delete()

    def createUser(self, tele):
        # self.model() 可以获取模型类构造函数
        user = self.model()
        user.telephone = tele
        user.save()


class User(models.Model):
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")
    # manage = UserManager()
    # 自定义新的objects对象 其实不是之前的objects对象了 只是指向一个名字相同的objects方便使用
    objects = UserManager()

    def __str__(self):
        return self.telephone

    class Meta:
        db_table = "用户类"
        ordering = ["id"]
        verbose_name = "用户模型类A"
        verbose_name_plural = "用户模型类B"
