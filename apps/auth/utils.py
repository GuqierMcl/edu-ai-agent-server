#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : utils.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/7 16:04 
@Version : 1.0
"""
from AAServer import redis_util
from AAServer.utils.redis_utils import CacheKeys
from apps.auth.models import User

from apps.permission.models import Permission


def get_user_perms_from_db(user) -> list:
    """
    从数据库获取用户权限
    :param user: 用户对象
    :return: set: 用户权限集合
    """
    if user.type == 0:  # 管理员
        # 超级管理员拥有所有权限
        qs = Permission.objects.all()
    else:
        qs = Permission.objects.filter(
            permissionrole__role__userrole__user=user,
            permissionrole__role__userrole__user__is_del=0
        ).values_list('name', flat=True).distinct()
    return list(set(qs))


def get_user_perms(user) -> list:
    """
    获取用户权限，使用缓存优化性能
    :param user: 用户对象
    :return: set: 用户权限集合
    """
    # 兼容 dict / User 实例
    user_id = user['id'] if isinstance(user, dict) else user.id

    user_info = redis_util.get_value(CacheKeys.USER_INFO + str(user_id))
    if user_info:
        perms = user_info['permissions']
    else:
        perms = get_user_perms_from_db(user if isinstance(user, User) else User.objects.get(id=user_id))
    return perms
