#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : serializers.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/11 17:19 
@Version : 1.0
"""
from rest_framework import serializers

from apps.auth.models import User
from apps.auth.utils import get_user_perms


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id",)

class UserInfoSerializer(serializers.ModelSerializer):
    """
    用户信息序列化器
    """
    permission_keys = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('password', 'is_del', 'create_time', 'update_time', 'create_user', 'update_user')

    def get_permission_keys(self, obj):
        return get_user_perms(obj)  # 转 list 方便 JSON

    def get_roles(self, obj):
        return ['admin']  # TODO: 获取用户角色列表，待实现