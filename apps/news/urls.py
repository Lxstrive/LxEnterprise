# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/14 16:32'
from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    # 新闻详情页
    path('<int:news_id>/', views.news_detail, name='news_detail'),
    # 首页新闻加载列表
    path('list/', views.news_list, name='news_list'),
    # 评论url
    path('public_comment/', views.public_comment, name='public_comment'),
]