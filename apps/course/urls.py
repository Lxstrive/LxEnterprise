# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/18 17:47'

from django.urls import path

from . import views

app_name = 'course'
urlpatterns = [
    # 课程首页
    path('', views.course_index, name='course_index'),
    # 课程详情页
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    # 课程视频播放获取token
    path('course_token/', views.course_token, name='course_token'),
    # 课程订单页
    path('course_order/<int:course_id>/', views.course_order,
         name='course_order'),
    # 订单的Key值
    path('course_order_key/', views.course_order_key, name="course_order_key"),
    path('notify_view/',views.notify_view,name='notify_view')
]
