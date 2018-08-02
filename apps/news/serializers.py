# !/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = '_X.xx_'
__date__ = '2018/7/24 22:31'

from rest_framework import serializers

from apps.news.models import News, NewsCategory, Comment, Banner
from apps.userauth.serializers import UserSerializer


class NewsCategorySerializer(serializers.ModelSerializer):
    """
        新闻分类序列化
    """

    class Meta:
        model = NewsCategory
        fields = ('id', 'name')


class NewsSerializer(serializers.ModelSerializer):
    """
        新闻序列化
    """
    category = NewsCategorySerializer()
    author = UserSerializer()

    class Meta:
        model = News
        fields = (
            'id', 'title', 'desc', 'thumbnail', 'pub_time', 'category',
            'author')


class CommentSerializer(serializers.ModelSerializer):
    """
        新闻评论序列化
    """
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'pub_time')


class BannerSerializer(serializers.ModelSerializer):
    """
        轮播图序列化
    """

    class Meta:
        model = Banner
        fields = ('id', 'image_url', 'priority', 'link_to')
