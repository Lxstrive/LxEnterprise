# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/18 16:44'

from django.http import JsonResponse


class HttpCode(object):
    ok = 200
    paramserror = 400
    unantu = 401
    methoderror = 405
    servererror = 500


def ok():
    return result()


def result(code=HttpCode.ok, message='', data=None, kwargs=None):
    json_dict = {'code': code, 'message': message, 'data': data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)


def params_error(message='', data=None):
    return result(code=HttpCode.paramserror, message=message, data=data)


def unauth(message='', data=None):
    return result(code=HttpCode.unantu, message=message, data=data)


def method_error(message='', data=None):
    return result(code=HttpCode.methoderror, message=message, data=data)


def server_error(message='', data=None):
    return result(code=HttpCode.servererror, message=message, data=data)
