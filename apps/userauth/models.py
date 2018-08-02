# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/14 18:13'

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
    BaseUserManager
from shortuuidfield import ShortUUIDField

from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('请输入手机号码')
        if not username:
            raise ValueError('请输入用户名')
        if not password:
            raise ValueError('请输入密码')
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, **kwargs):
        # 创建普通用户
        # 方便测试创建的用户都是超级用户可以使用后台管理
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone, username, password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        # 创建超级用户
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone, username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """
        用户模型
    """
    #  pip install django-shortuuidfield
    #  使用uuid做为主键
    uid = ShortUUIDField(primary_key=True)
    telephone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, verbose_name='邮箱', null=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, verbose_name='是否可用')
    is_staff = models.BooleanField(default=False)
    add_time = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'
    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
