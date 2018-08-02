# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/7/14 19:27'


class FormMixin(object):
    """
        获取表单错误
    """

    def get_errors(self):
        if hasattr(self, 'errors'):
            errors = self.errors.get_json_data()
            new_errors = {}
            for key, message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}
