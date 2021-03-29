from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Goods, GoodsCategory
from .filters import GoodsFilter
from .serializer import GoodsSerializer,CategorySerializer


# Create your views here.


# 此类定义后，setting文件无需再配置
class GoodsPagination(PageNumberPagination):
    page_size = 10
    # 第多少页
    page_size_query_param = 'page_size'
    # 第多少条
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    List all goods
    商品列表分页，查询，过滤，排序
    """
    # def get(self,request,format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods,many=True)
    #     return Response(goods_serializer.data)
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['name', 'shop_price']
    filter_class = GoodsFilter
    search_fields = ['name', 'goods_desc', 'goods_brief']
    ordering_fields = ['shop_price','sold_num']


class CategoryListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type = 1)
    serializer_class = CategorySerializer
