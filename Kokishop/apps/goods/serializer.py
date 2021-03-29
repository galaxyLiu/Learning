#!/user/bin/env python
# -*- coding:utf-8 -*-

from rest_framework import serializers
from goods.models import Goods,GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100, required=True)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()
    # 外键，覆盖默认的外键category
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"


