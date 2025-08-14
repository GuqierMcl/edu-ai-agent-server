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
from django.core.validators import RegexValidator
from rest_framework import serializers

from AAServer import constants
from apps.auth.models import User
from apps.auth.utils import get_user_perms
from apps.resource.models import Resource
from apps.resource.serializers import ResourceSerializer

class UserInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_del', 'create_user', 'create_time', 'update_time', 'update_user')   # 不暴露敏感字段

class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(write_only=True, validators=[
        RegexValidator(
            regex=constants.User.USER_PASSWORD_REGEX,
            message='密码必须 8-20 位，且包含字母、数字'
        )
    ])

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id",)

    def get_avatar_url(self, obj):
        avatar_id = obj.avatar if isinstance(obj, User) else obj['avatar']
        if avatar_id:
            resource = Resource.objects.get(id=avatar_id)
            url = ResourceSerializer(resource).data['remote_file_url']
            return url
        return None

class UserInfoSerializer(UserSerializer):
    """
    用户信息序列化器
    """
    permission_keys = serializers.SerializerMethodField(read_only=True)
    roles = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = User
        exclude = ('password', 'is_del', 'create_time', 'update_time', 'create_user', 'update_user')

    def get_permission_keys(self, obj):
        return get_user_perms(obj)  # 转 list 方便 JSON

    def get_roles(self, obj):
        return ['admin']  # TODO: 获取用户角色列表，待实现
