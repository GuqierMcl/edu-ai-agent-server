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
from apps.resource.models import Resource
from apps.resource.serializers import ResourceSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id",)

class UserInfoSerializer(serializers.ModelSerializer):
    """
    用户信息序列化器
    """
    permission_keys = serializers.SerializerMethodField(read_only=True)
    roles = serializers.SerializerMethodField(read_only=True)
    avatar_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = ('password', 'is_del', 'create_time', 'update_time', 'create_user', 'update_user')

    def get_permission_keys(self, obj):
        return get_user_perms(obj)  # 转 list 方便 JSON

    def get_roles(self, obj):
        return ['admin']  # TODO: 获取用户角色列表，待实现

    def get_avatar_url(self, obj):
        if obj['avatar']:
            resource = Resource.objects.get(id=obj['avatar'])
            url = ResourceSerializer(resource).data['remote_file_url']
            return url
        return None
