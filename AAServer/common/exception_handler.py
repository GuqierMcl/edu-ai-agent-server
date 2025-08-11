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
import logging

from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
from rest_framework.views import exception_handler

from AAServer.common import exceptions
from AAServer.response import ResponseEnum, R

logger = logging.getLogger("AAServer")
def common_exception_handler(exc, context):
    """
    通用异常处理
    :param exc:
    :param context:
    :return:
    """
    response = exception_handler(exc, context)
    print('异常信息:', exc)
    logger.error(context["view"])
    logger.error(context["request"])
    logger.error(context["request"].path)
    logger.error(context["request"].method)

    # 处理自定义异常
    if isinstance(exc, AuthenticationFailed):
        return R.fail(ResponseEnum.INVALID_TOKEN)
    if isinstance(exc, NotAuthenticated):
        return R.fail(ResponseEnum.USER_NOT_LOGIN)

    # 处理其他异常
    if response is not None:
        response = R.fail(ResponseEnum.SYSTEM_ERROR, data=response.data)
    else:
        response = R.fail(ResponseEnum.SYSTEM_ERROR)
    return response