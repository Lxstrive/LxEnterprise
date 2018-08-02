# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/14 18:59'

from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import redirect, reverse
from django.contrib.auth import get_user_model

from .forms import LoginForm, RegisterForm
from utils import restful

User = get_user_model()


@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request, username=telephone, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.ok()
            else:
                return restful.unauth(message='您的账号已冻结')
        else:
            return restful.params_error(message='手机号或密码错误')
    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)


def logout_view(request):
    # 退出登录
    logout(request)
    return redirect(reverse('index'))


@require_POST
def register(request):
    # 注册
    form = RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        username = form.cleaned_data.get('username')
        password = request.POST.get('password1')
        user = User.objects.create_user(telephone=telephone, username=username,
                                        password=password)
        login(request, user)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())