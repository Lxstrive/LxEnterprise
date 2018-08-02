# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/14 17:24'

from django.urls import path
from . import views

# 后台管理页配置
app_name = 'cms'

urlpatterns = [
    # 后台首页
    path('', views.index, name='index'),
    # 发布新闻
    path('write_news/', views.WriteNewsView.as_view(), name='write_news'),
    # 新闻分类
    path('news_category/', views.news_category, name='news_category'),
    # 添加分类
    path('add_news_category/', views.add_news_category,
         name='add_news_category'),
    # 编辑分类
    path('edit_news_category/', views.edit_news_category,
         name='edit_news_category'),
    # 删除分类
    path('delete_news_category/', views.delete_news_category,
         name='delete_news_category'),
    # 上传图片
    path('upload_file/', views.upload_file, name='upload_file'),
    # 轮播图
    path('banners/', views.banners, name='banners'),
    # 添加轮播图
    path('add_banner/', views.add_banner, name='add_banner'),
    # 轮播图列表序列化
    path('banner_list/', views.banner_list, name='banner_list'),
    # 删除轮播图
    path('delete_banner/', views.delete_banner, name='delete_banner'),
    # 编辑轮播图
    path('edit_banner/', views.edit_banner, name='edit_banner'),
    # 新闻列表页
    path('news_list/', views.NewsListView.as_view(), name='news_list'),
    # 编辑新闻
    path('edit_news/', views.EditNewsView.as_view(), name='edit_news'),
    # 删除新闻
    path('delete_news/', views.delete_news, name='delete_news'),
    # 发布课程
    path('public_course/', views.PubCourse.as_view(), name='public_course'),
]
