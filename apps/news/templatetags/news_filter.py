# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/24 21:52'
from datetime import datetime
from django import template
from django.utils.timezone import now as now_func
register = template.Library()


@register.filter
def time_since(value):
    if not isinstance(value, datetime):
        return value
    now = now_func()
    timestamp = (now - value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif timestamp >= 60 and timestamp < 60 * 60:
        minutes = int(timestamp / 60)
        return '%s 分钟前' % minutes
    elif timestamp >= 60 * 60 and timestamp < 60 * 60 * 24:
        hours = int(timestamp / 60 / 60)
        return '%s 小时前' % hours
    elif timestamp >= 60 * 60 * 24 and timestamp < 60 * 60 * 24 * 30:
        days = int(timestamp / 60 / 60 / 24)
        return '%s 天前' % days
    else:
        return value.strftime('%Y/%m/%d %H:%M')