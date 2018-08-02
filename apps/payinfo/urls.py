# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/18 18:11'

from django.urls import path
from . import views

app_name = 'payinfo'

urlpatterns = [
    path('', views.payinfo, name='payinfo'),
    path('auth/', views.auth_test)
]