#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
全局异常处理
@Project : AAServer 
@File    : exception_handler.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/6 14:14 
@Version : 1.0
"""
from rest_framework.views import exception_handler

from AAServer.response import ResponseEnum


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {
            "code": ResponseEnum.SYSTEM_ERROR.code,
            "msg": ResponseEnum.SYSTEM_ERROR.msg,
        }
    return response