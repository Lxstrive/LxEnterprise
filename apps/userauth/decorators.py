# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/26 17:48'

from django.shortcuts import redirect
from utils import restful


def user_login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            if request.is_ajax():
                return restful.unauth(message='请先登录')
            else:
                return redirect('/')
    return wrapper
