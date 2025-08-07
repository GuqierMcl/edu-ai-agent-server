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

from apps.auth.models import Permission

def get_user_perms_from_db(user) -> list:
    """
    从数据库获取用户权限
    :param user: 用户对象
    :return: set: 用户权限集合
    """
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
    user_info = redis_util.get_value(CacheKeys.USER_INFO + user.id)
    perms = user_info['permissions']
    if perms is None:
        perms = get_user_perms_from_db(user)
    return perms