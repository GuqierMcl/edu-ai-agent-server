#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
全局异常处理
@Project : AAServer 
@File    : exception.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/6 14:14 
@Version : 1.0
"""
import logging

from rest_framework.views import exception_handler

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
    logger.error(exc)
    logger.error(context["view"])
    logger.error(context["request"])
    logger.error(context["request"].path)
    logger.error(context["request"].method)
    if response is not None:
        response = R.fail(ResponseEnum.SYSTEM_ERROR, data=response.data['detail'])
    else:
        response = R.fail(ResponseEnum.SYSTEM_ERROR)
    return response