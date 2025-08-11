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
import uuid

from django.forms import model_to_dict

from AAServer import redis_util
from AAServer.utils.redis_utils import CacheKeys
from apps.auth.utils import get_user_perms_from_db


def do_login(user, request):
    """
    处理登录
    :param request: 请求对象
    :param user: 登录用户
    :return: 登录信息
    """
    # 生成AccessToken
    access_token = uuid.uuid4()

    # 获取用户权限
    permissions = get_user_perms_from_db(user)

    # 存入缓存
    user_info = model_to_dict(user, exclude=['create_time', 'update_time', 'password', 'create_user', 'update_user', 'is_del', 'expire_time', 'last_login_time'])
    user_info['permissions'] = permissions
    redis_util.set_object(CacheKeys.TOKEN_USER + str(access_token), user_info, timeout=3600 * 24)  # 有效期为24小时

    # 响应结果
    return {
        'token': str(access_token),
    }