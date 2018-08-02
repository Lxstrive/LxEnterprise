# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/14 19:02'

from django import forms

from captcha.fields import CaptchaField
from apps.forms import FormMixin
from .models import User


class LoginForm(forms.Form, FormMixin):
    """
        登录验证
    """
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20, min_length=6,
                               error_messages={'max_length': '密码最长不能超过20个字符',
                                               'min_length': '密码最少不能少于6个字符'})
    remember = forms.IntegerField(required=False)


class RegisterForm(forms.Form, FormMixin):
    """
        注册验证
    """
    telephone = forms.CharField(max_length=11)
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=20, min_length=6,
                                error_messages={'max_length': '密码最长不能超过20个字符',
                                                'min_length': '密码最少不能少于6个字符'})
    password2 = forms.CharField(max_length=20, min_length=6,
                                error_messages={'max_length': '密码最长不能超过20个字符',
                                                'min_length': '密码最少不能少于6个字符'})

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        telephone = cleaned_data.get('telephone')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('两次密码输入不一致')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError('手机号码已存在')
