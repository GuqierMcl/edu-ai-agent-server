#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : decorators.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/11 13:41 
@Version : 1.0
"""
import functools


def req_path(path):
    """
    获取请求路径装饰器
    :return:
    """
    def decorator(func):
        func.path = path          # 把属性挂上去
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator