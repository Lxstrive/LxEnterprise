# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/24 22:41'

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'telephone', 'username', 'email', 'is_active', 'is_staff')