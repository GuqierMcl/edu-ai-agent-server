#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : services.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/6 17:19 
@Version : 1.0
"""
from AAServer import redis_connect


def do_login(user, request):
    """
    处理登录
    :param request: 请求对象
    :param user: 登录用户
    :return: 登录信息
    """
    redis_connect
