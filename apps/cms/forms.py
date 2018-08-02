# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/23 23:30'

from apps.forms import FormMixin
from django import forms

from apps.news.models import News, Banner
from apps.course.models import Course


class EditNewsCategory(forms.Form):
    """
        编辑新闻分类
    """
    pk = forms.IntegerField(error_messages={'required': '必须传入分类的ID'})
    name = forms.CharField(max_length=100)


class WriteNewsForm(forms.ModelForm, FormMixin):
    """
        发布新闻
    """
    category = forms.IntegerField()

    class Meta:
        model = News
        exclude = ['category', 'author', 'pub_time']


class EditNewsForm(forms.ModelForm, FormMixin):
    """
        编辑新闻
    """
    category = forms.IntegerField()
    pk = forms.IntegerField()

    class Meta:
        model = News
        exclude = ['category', 'author', 'pub_time']


class AddBannerForm(forms.Form, FormMixin):
    """
        添加轮播图
    """

    class Meta:
        model = Banner
        fields = ('priority', 'link_to', 'image_url')


class EditBannerForm(forms.Form, FormMixin):
    """
        编辑轮播图
    """
    pk = forms.IntegerField()

    class Meta:
        model = Banner
        fields = ('priority', 'link_to', 'image_url')


class PubCourseForm(forms.ModelForm):
    """
        发布课程
    """
    category_id = forms.IntegerField()
    teacher_id = forms.IntegerField()

    class Meta:
        model = Course
        exclude = ['category', 'teacher']