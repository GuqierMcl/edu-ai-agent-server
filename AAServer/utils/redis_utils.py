#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : redis_utils.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/6 17:32 
@Version : 1.0
"""
import json

class RedisUtil:
    def __init__(self, redis_connect):
        self.conn = redis_connect

    def set_value(self, key, value, timeout=None):
        self.conn.set(key, value, timeout)

    def get_value(self, key):
        return self.conn.get(key)

    def delete_value(self, key):
        self.conn.delete(key)

    def get_all_keys(self, pattern='*'):
        return self.conn.keys(pattern)

    def set_object(self, key, obj, timeout=None):
        self.conn.set(key, json.dumps(obj), timeout)

    def get_object(self, key):
        return json.loads(self.conn.get(key))

class CacheKeys:
    TOKEN_USER = 'AUTH:TOKEN_USER:'          # token对应的用户信息缓存
    USER_INFO = 'AUTH:USER_INFO:'                # 用户信息缓存
    USER_PERMISSIONS = 'AUTH:PERMISSION:'  # 用户权限缓存