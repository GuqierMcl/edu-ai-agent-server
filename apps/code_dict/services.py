#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : services.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/14 15:25 
@Version : 1.0
"""
from apps.code_dict.models import Code

def get_code_name_by_type_and_code(code, code_type):
    """
    根据类型和代码获取名称
    :param code: 代码
    :param code_type: 类型
    :return: 名称
    """
    try:
        instance = Code.objects.get(code=code, type=code_type)
        return instance.name
    except Code.DoesNotExist:
        return None