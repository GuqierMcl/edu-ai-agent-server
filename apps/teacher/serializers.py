#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : serializers.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/13 15:47 
@Version : 1.0
"""
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import serializers

from AAServer import constants
from apps.auth.models import User
from apps.code_dict.services import get_code_name_by_type_and_code
from apps.teacher.models import Teacher
from apps.user.serializers import UserInlineSerializer
from apps.user.services import create_user_by_validated_data, update_user_by_validated_data


class TeacherSerializer(serializers.ModelSerializer):
    user = UserInlineSerializer(read_only=True)
    profession_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Teacher
        fields = ('id', 'user', 'stu_friendly_name', 'profession', 'profession_name', 'department', 'create_time', 'update_time')

    def get_profession_name(self, obj):
        return get_code_name_by_type_and_code(obj.profession, constants.CodeDict.CODE_TEACHER_PROFESSION)

class TeacherCreateSerializer(serializers.Serializer):
    # 用户字段
    account  = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    name     = serializers.CharField(max_length=255, allow_blank=True)
    nickname = serializers.CharField(max_length=255, allow_blank=True)
    phone    = serializers.CharField(max_length=255, required=False, allow_blank=True)
    email    = serializers.CharField(max_length=255, required=False, allow_blank=True)

    # 教师字段
    stu_friendly_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    profession        = serializers.IntegerField()
    department        = serializers.CharField(max_length=100, required=False, allow_blank=True)

    @transaction.atomic
    def create(self, validated_data):
        # 1. 先创建用户
        _user, _data = create_user_by_validated_data(validated_data, user_type=constants.UserDict.USER_TYPE_TEACHER)  # 固定教师角色

        # 2. 再创建教师
        teacher = Teacher.objects.create(
            user=_user,
            **validated_data,
        )
        return teacher

class TeacherFlatUpdateSerializer(serializers.ModelSerializer):
    # 把 user 表字段“平铺”到顶层
    nickname = serializers.CharField(required=False, allow_blank=False)
    name     = serializers.CharField(required=False, allow_blank=False)
    phone    = serializers.CharField(required=False, allow_blank=False)
    email    = serializers.CharField(required=False, allow_blank=False)

    class Meta:
        model = Teacher
        fields = (
            'stu_friendly_name', 'profession', 'department',
            'nickname', 'name', 'phone', 'email'
        )

    @transaction.atomic
    def update(self, instance, validated_data):
        # 1. 更新用户信息
        _user, _data = update_user_by_validated_data(instance.user, validated_data)

        # 2. 更新教师
        for k, v in validated_data.items():
            if k == 'user':
                setattr(instance, k, _user)
            else:
                setattr(instance, k, v)
        instance.save()
        return instance