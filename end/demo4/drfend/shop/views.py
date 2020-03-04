from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, filters

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from shop.pagination import MyPagination
from shop.throttling import MyAnon, MyUser
from . import permissions as mypermissions
from .models import *
from .serializers import *
from rest_framework import throttling


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承viewsets.ModelViewSet 之后用于GET POST PATCH DELETE等HTTP动词操作
    serializer_class 指明序列化类
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # 超级管理员才能创建分类 普通用户只能查看
    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or \
                self.action == "destory":
            return [permissions.IsAdminUser()]  # 必须是超级管理员
            # return [permissions.IsAuthenticatedOrReadOnly()]  # 未登录只读，登陆后可修改
            # return [mypermissions.CategoryPermission()]  # 使用自定义权限类
        else:
            # return [permissions.IsAuthenticated()]
            return []

    # 控制访问频次
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [MyAnon, MyUser]
    # 设定分页
    pagination_class = MyPagination
    # 局部过滤配置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    # 局部搜索配置
    search_fields = ["name"]
    # 局部排序配置
    ordering_fields = ["id"]


class GoodViewsSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodImagesViewsSets(viewsets.ModelViewSet):
    queryset = GoodImages.objects.all()
    serializer_class = GoodImagesSerializer


class UserViewsSets1(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    """
    声明用户操作  获取 添加 更新 删除
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 添加自定义注册路由
    @action(methods=['POST'], detail=False)
    def register(self, request):
        seria = UserRegisterSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        # return Response("创建成功")
        return Response(seria.data, status=status.HTTP_201_CREATED)


class UserViewsSets(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
    声明用户操作 获取 更新 删除
    此处更新的用户密码是没有加密的
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        print("", self.action)
        if self.action == "create":
            return UserRegisterSerializer
        return UserSerializer


class OrderViewsSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [permissions.OrdersPermission]

    def get_permissions(self):
        print("当前http方法为", self.action)
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or \
                self.action == 'retrieve' or self.action == "destroy":
            return [mypermissions.OrdersPermission()]
        else:
            return [permissions.IsAdminUser()]


# 使用视图函数  调用装饰器api_view
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == "GET":
        # instance 为需要序列化的对象，来源于数据库
        seria = CategorySerializer(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # data 为序列化的对象 来源于请求中提取的数据
        # data 从请求中获取数据  instance从数据库取
        seria = CategorySerializer(data=request.data)
        # 对请求中提取的数据序列化之前进行校检
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def category_detail(request, cid):
    model = get_object_or_404(Category, pk=cid)
    if request.method == "GET":
        seria = CategorySerializer(instance=model)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH" or request.method == "PUT":
        # data 从请求中获取数据  instance从数据库取
        seria = CategorySerializer(instance=model, data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse("当前路由不允许" + request.method + '操作')


class CategoryListView1(APIView):
    """
    继承DRF自带的APIView类 即可完成请求相应的封装
    """

    def get(self, request):
        # return HttpResponse("返回列表成功")
        seria = CategorySerializer(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)

    def post(self, request):
        # return HttpResponse("创建成功")
        seria = CategorySerializer(data=request.data)
        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)
        # 升级代码
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)

    pass


class CategoryDetailView1(APIView):
    def get(self, request, cid):
        # return HttpResponse("返回单个对象成功")

        model = get_object_or_404(Category, pk=cid)
        seria = CategorySerializer(instance=model)
        return Response(seria.data, status=status.HTTP_200_OK)

    def put(self, request, cid):
        # return HttpResponse("put修改成功")
        model = get_object_or_404(Category, pk=cid)
        # data 从请求中获取数据  instance从数据库取
        seria = CategorySerializer(instance=model, data=request.data)
        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)
        # 升级代码
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)

    def patch(self, request, cid):
        # return HttpResponse("patch修改成功")
        model = get_object_or_404(Category, pk=cid)
        # data 从请求中获取数据  instance从数据库取
        seria = CategorySerializer(instance=model, data=request.data)
        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)
        # 升级代码
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)

    def delete(self, request, cid):
        # return HttpResponse("删除成功")
        model = get_object_or_404(Category, pk=cid)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        return self.list(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# 上面两个类组合到一起  需要两个路由
#     url(r'^zoos/$',ZooListView.as_view()),
#     url(r'zoos/(?P<pk>\d+)/',ZooDetailView.as_view()),
# 升级视图集，继承模型视图集 只需一个路由，但是需要注册
# from rest_framework import routers
# router = routers.DefaultRouter()
# url('',include(router.urls)),
