# 模型M
##  ORM
### 一、MVC 与 ORM
MVC框架中包括一个重要的部分，就是ORM，它实现了数据模型与数据库的解耦，即数据模型的设计不需要依赖于特定的数据库，通过简单的配置就可以轻松更换数据库，比如我们之前搭建的快速开发项目，就不需要考虑数据库的问题


**ORM是“对象-关系-映射”的简称**，主要任务是：
1，对象的类型生成表结构
2，将对象、列表的操作，转换为sql语句
3，将sql查询到的结果转换为对象、列表
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215092844349.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
这极大的减轻了开发人员的工作量，不需要面对因数据库变更而导致的无效劳动
**Django中的模型包含存储数据的字段和约束，对应着数据库中唯一的表**


### 二、ORM分为两种：
1，DB First 数据库里先创建数据库表结构，根据表结构生成类，根据类操作数据库
2，**Code First 先写代码，执行代码创建数据库表结构**
**主流的orm都是code first。**
django 的orm也是code first，所以学的时候，本质就分为两块：
1，根据类自动创建数据库表
**python manage.py makemigrations**
2，根据类对数据库表中的数据进行各种操作

### 三、优缺点：
优点：
摆脱复杂的SQL操作，适应快速开发；
让数据结构变得简洁；
数据库迁移成本更低


*Django中自带了ORM ，如果我更熟悉其他的ORM，怎么办？
缺点：
Django框架中ORM与其他模块耦合度较高，不能使用其他ORM框架，这就是一个大Bug*

## 模型定义
### 一，定义属性
1，在模型中定义的属性，会生成表中的字段
2，定义属性时，需要字段类型，字段类型被定义在django.db.models.fields目录下
3，django会为表增加自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后，则django不会再生成默认的主键列

属性命名限制
不能是python的保留关键字
由于django的查询方式，不允许使用连续的下划线

使用方式
1.  导入from django.db import models
2.  通过models. Field创建字段类型的对象，赋值给属性

### 二，字段类型
AutoField：一个根据实际ID自动增长的IntegerField，通常不指定，如果不指定，一个主键字段将自动添加到模型中

BooleanField：true/false 字段，此字段的默认表单控制是CheckboxInput
NullBooleanField：支持null、true、false三种值

CharField(max_length=字符长度)：字符串，默认的表单样式是 TextInput
TextField：大文本字段，一般超过4000使用，默认的表单控件是Textarea

IntegerField：整数
FloatField：用Python的float实例来表示的浮点数
DecimalField(max_digits=None, decimal_places=None)：使用python的Decimal实例表示的十进制浮点数
DecimalField.max_digits：位数总数
DecimalField.decimal_places：小数点后的数字位数

DateField[auto_now=False, auto_now_add=False])：使用Python的datetime.date实例表示的日期
参数DateField.auto_now：每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false
参数DateField.auto_now_add：当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false
该字段默认对应的表单控件是一个TextInput
在管理员站点添加了一个JavaScript写的日历控件，和一个“Today"的快捷按钮
auto_now_add, auto_now, and default 这些设置是相互排斥的，他们之间的任何组合将会发生错误的结果

TimeField：使用Python的datetime.time实例表示的时间，参数同DateField
DateTimeField：使用Python的datetime.datetime实例表示的日期和时间，参数同DateField


FileField：一个上传文件的字段
ImageField：继承了FileField的所有属性和方法，但对上传的对象进行校验，确保它是个有效的image

### 三，字段选项
通过字段选项，可以实现对字段的约束，在定义字段对象时通过关键字参数指定

verbose_name：在admin界面显示的字段标识
null：如果为True，Django 将空值以NULL 存储到数据库中，默认值是 False
blank：如果为True，则该字段允许为空白，默认值是 False
对比：null是数据库范畴的概念，blank是表单验证证范畴的

db_column：字段的名称，如果未指定，则使用属性的名称
db_index：若值为 True, 则在表中会为此字段创建索引
default：默认值
primary_key：若为 True, 则该字段会成为模型的主键字段
unique：如果为 True, 这个字段在表中必须有唯一值
help_text：会在form表单控件中显示help文本
choices：Admin中选择框的内容
editable            Admin中是否可以编辑


### 四，元选项

在模型类中定义类Meta，用于设置元信息，对应于数据库中表信息

app_label：指明该模型属于哪一个应用
db_table：定义数据表名称，推荐使用小写字母，数据表的默认名称<app_name>_<model_name>
ordering：对象的默认排序字段，获取对象的列表时使用，接收属性构成的列表
verbose_name：Admin显示模型名
verbose_name_plural：Admin显示模型名附属



### 五，自定义管理类
class BookManage(models.Manager):
    def setprice(self,book,price):
        if isinstance(book,self.model):
            book.price = price
            book.save()
        else:
            raise Exception(f"{book}并非{self.model}实例")

 # Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_time = models.DateField()
    price = models.DecimalField(max_digits=6,decimal_places=3)
    manage =BookManage()

具体操作
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215110706487.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215110742316.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215110842654.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215112104126.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
### 六，关系
关系的类型包括
==ForeignKey：一对多，将字段定义在多的端中
ManyToManyField：多对多，将字段定义在任意一端中
OneToOneField：一对一，将字段定义在任意一端中==

**1，一对多案例：**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215114114727.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)


**2，一对一案例：**
在我们自己的项目中需要使用到用户系统，然而django自带了用户系统，并且定义了很多常用字段，此时我们就可以使用一对一关系

如：银行卡号和银行用户
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215143647159.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020021514351958.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)

**3，多对多案例：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215145624351.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
 **添加关系 t.articles.add(a) 删除t.acticles.remove(a)
  未重命名查询 a.tag_set.all()    t.acticles.all()
  重命名查询 a.tags.all()    t.acticles.all()**![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215151057349.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
**总结一下一对一,一对多，多对多之间的关联查询**

	
	
	# 一对多   一方Book  实例b  多方Hero  实例h    关系字段定义在多方
	# 一找多    b.hero_set.all()    如果定义过related_name='heros' 则使用  b.heros.all()
	# 多找一   h.book
	# 一对一   一方Account  实例a   一方Concact 实例c   关系字段定义在任意一方
	# a 找 c  a.concact
	# c 找 a  c.account
	
	# 多对多  多方Article  实例a    多方Tag 实例t   关系字段可以定义在任意一方
	# 添加关系   t.articles.add(a)    移除关系  t.articles.remove(a)
	# a 找 所有的 t   a.tag_set.all()   如果定义过related_name='tags' 则使用 a.tags.all()
	# t 找 所有的 a   t.articles.all()


## 模型查询
一、查询集与过滤器
查询集表示从数据库中获取的对象集合，查询集是可迭代的对象
返回查询集的方法，称为过滤器，过滤器基于所给的参数限制查询的结果
从Sql的角度，查询集和select语句等价，过滤器像where和limit子句

查询集经过过滤器筛选后返回新的查询集，因此可以写成链式过滤

惰性执行：创建查询集不会带来任何数据库的访问，直到调用数据时，才会访问数据库

**1，返回新的查询集：**
all() ：检索所有的对象  
filter(**kwargs) ：检索特定的对象 返回一个与参数匹配的QuerySet 
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215164027894.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
exclude()：返回一个与参数不匹配的QuerySet 
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215164121562.png)
order_by(column_name)：检索排序后的对象，column_name:排序的列，默认升序，列名前加- 降序排序 

**2，返回单个对象**
get()：返回单个满足条件的对象，
如果未找到会引发"模型类.DoesNotExist"异常 
如果多条被返回，会引发"模型类.MultipleObjectsReturned"异常 
![在这里插入图片描述](https://img-blog.csdnimg.cn/202002151644269.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
count()：返回当前查询的总条数 
first()：返回第一个对象 
last()：返回最后一个对象 
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215164658894.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
exists()：判断查询集中是否有数据，如果有则返回True


**3，限制查询集**
查询集返回列表，可以使用下标的方式进行限制
等同于sql中的limit 和offset子句
==注意：不支持负数索引==

使用下标后返回一个新的查询集，不会立即执行查询

如果获取一个对象，直接使用[0]，等同于[0:1].get()
BookInfo.objects.all()[:5]
查找前5个entry表里的数据
BookInfo.objects.all()[5:10]
查找从第5个到第10个之间的数据。
BookInfo.objects.all()[:10:2]
查询从第0个开始到第10个，步长为2的数据。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215164849932.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
**4，字段查询**
实现where子名，作为方法filter()、exclude()、get()的参数
语法：属性名称_ _比较运算符=值
表示两个下划线，左侧是属性名称，右侧是比较类型


比较运算符
exact：表示判等
如果没有写“比较运算符”，表示判等
Book.objects.filter(id__exact=1)


contains：是否包含，大小写敏感
exclude(title__contains='传')


startswith、endswith：以value开头或结尾，大小写敏感
exclude(title__endswith='传')
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215165217288.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)

isnull、isnotnull：是否为null
filter(title__isnull=False)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215165341953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)

**在前面加个==i==表示不区分大小写，如iexact、icontains、istarswith、iendswith**

in：是否包含在范围内
filter(pk__in=[1, 2, 3, 4, 5])

gt、gte、lt、lte：大于、大于等于、小于、小于等于
filter(id__gt=3)

year、month、day、week_day、hour、minute、second：对日期间类型的属性进行运算
filter(bpub_date__year=1980)
filter(bpub_date__gt=date(1980, 12, 31))
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215162658813.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
查询的快捷方式：pk，pk表示primary key，默认的主键是id
filter(pk__lt=6)

**5，聚合函数**
使用aggregate()函数返回聚合函数的值
函数：Avg，Count，Max，Min，Sum
from django.db.models import Max
maxDate = Book.objects.all().aggregate(Max('pub_date'))

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215162021785.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)

6，F对象
F()允许Django在未实际链接数据的情况下具有对数据库字段的值的引用。
场景
Python操作方式
通常情况下我们在更新数据时需要先从数据库里将原数据取出后放在内存里，然后编辑某些属性，最后提交。
book = Book.objects.get(pk=3) 
delta = timedelta(days=3) 
book.pub_date = book.pub_date + delta 
book.save() 
book = Book.objects.get(pk=3) 
print(book.pub_date)


当我们使用了F()之后呢？
from django.db.models import F
book = Book.objects.get(pk=3) 
delta = timedelta(days=3) 
book.pub_date = F('pub_date') + delta 
book.save() 
book = Book.objects.get(pk=3) 
print(book.pub_date)

结论
当Django程序中出现F()时，Django会使用SQL语句的方式取代标准的Python操作。
上述代码中不管book.pub_date的值是什么，Python都不曾获取过其值，python做的唯一的事情就是通过Django的F()函数创建了一条SQL语句然后执行而已。
实质上通过F对象减少了一次与数据库的交互。
特别是并发的情况，效率也变高了，减少了多线程同时操作带来的隐患。
可以使用模型的字段A与字段B进行比较，如果A写在了等号的左边，则B出现在等号的右边，需要通过F对象构造
filter(pk__lt=F('price'))


7，Q对象
应用场景
一般我们在Django程序中查询数据库操作都是在QuerySet里进行进行，例如下面
代码:
q1 = Book.objects.filter(pub_date__gt=date(1992, 1, 1))
q2 = q1.exclude(pk__gt=2)

将其组合起来:
q = Book.objects.filter(bpub_date__gt=date(1992, 1,1)).exclude(pk__gt=2)

问题：复杂的查询条件，导致查询越来越长。

引入Q对象
Q()对象就是为了将这些条件组合起来。
当我们在查询的条件中需要组合条件时(例如两个条件“且”或者“或”)时。我们可以使用Q()查询对象。

&（与）或者|（或）~（非）
可以将多个Q()对象组合起来传递给filter()，exclude()，get()等函数。
当操作符应用在两个Q对象时，会产生一个新的Q对象
结合括号进行分组，构造复杂的Q对象
Q(pub_date__gt=date(1992, 1, 1)) & ~Q(title__startswith="笑")
改写一下 
c1 = Q(pub_date__gt=date(1992, 1, 1)) 
c2 = Q(title__startswith="笑") 
q= BookInfo.books.filter(c1 & ~c2 )



![在这里插入图片描述](https://img-blog.csdnimg.cn/20200215172058608.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQzOTI0NA==,size_16,color_FFFFFF,t_70)
























