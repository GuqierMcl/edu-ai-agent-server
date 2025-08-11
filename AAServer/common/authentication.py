#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : authentication.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/11 14:15 
@Version : 1.0
"""
import json

from rest_framework.authentication import TokenAuthentication

from AAServer import redis_util
from AAServer.common import exceptions
from AAServer.utils.redis_utils import CacheKeys
from apps.auth.models import User


class RedisTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user_data = redis_util.get_value(CacheKeys.TOKEN_USER + str(key))
        if user_data:
            user_dict = json.loads(user_data)
            user_obj = User()
            for key_name in user_dict.keys():
                setattr(user_obj, key_name, user_dict[key_name])
            return user_obj, key
        raise exceptions.AuthenticationFailed
