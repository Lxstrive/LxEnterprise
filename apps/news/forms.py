# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/26 15:48'


from django import forms
from apps.forms import FormMixin


class PublicCommentForm(forms.Form, FormMixin):
    """
        发布评论表单
    """
    content = forms.CharField()
    news_id = forms.IntegerField()