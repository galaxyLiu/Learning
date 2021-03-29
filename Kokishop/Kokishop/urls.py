"""Kokishop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

import xadmin
from Kokishop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

# from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet,CategoryListViewSet

# goods_list = GoodsListViewSet.as_view({'get': 'list'})
router = routers.SimpleRouter()
router.register(r'goods', GoodsListViewSet,basename='goods')
router.register(r'categorys', CategoryListViewSet,basename='categorys')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('xadmin/', xadmin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    # drf自带的认证模式
    url(r'^api-token-auth/',views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/',obtain_jwt_token),

    #商品列表页
    url(r'^',include(router.urls)),
    # url(r'goods/$',goods_list,name='goods-list'),

    url(r'docs/',include_docs_urls(title='超级生鲜')),


]
