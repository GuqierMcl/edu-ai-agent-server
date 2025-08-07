#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : authentication.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/7 16:56 
@Version : 1.0
"""
from rest_framework.authentication import TokenAuthentication


class RedisTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user_data = redis_connect.get(key)
        if user_data:
            user_dict = json.loads(user_data)
            user_obj = User()
            for key_name in user_dict.keys():
                setattr(user_obj, key_name, user_dict[key_name])
            return user_obj, key
        raise exceptions.AuthenticationFailed(_('无效的token.'))
