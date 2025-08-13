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

from apps.auth.models import User
from apps.teacher.models import Teacher

class UserInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_del', 'create_user', 'create_time', 'update_time', 'update_user')   # 不暴露敏感字段


class TeacherSerializer(serializers.ModelSerializer):
    user = UserInlineSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ('id', 'user', 'stu_friendly_name', 'profession', 'department', 'create_time', 'update_time')

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
        password = validated_data.pop('password')
        user_fields = {k: validated_data.pop(k) for k in list(validated_data) if k in ['account', 'name', 'nickname', 'phone', 'email']}
        user = User.objects.create(
            type=1,                         # 固定教师角色
            **user_fields,
            password=make_password(password),
        )

        # 2. 再创建教师
        teacher = Teacher.objects.create(
            user=user,
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
        # 1. 拆出用户字段
        user_fields = {}
        for key in ('nickname', 'name', 'phone', 'email'):
            if key in validated_data:
                user_fields[key] = validated_data.pop(key)

        # 2. 更新用户
        user = instance.user
        print(user_fields)
        print(validated_data)
        if user_fields:
            print("修改用户信息:", user_fields)
            for k, v in user_fields.items():
                setattr(instance.user, k, v)
            instance.user.save()

        # 3. 更新教师
        for k, v in validated_data.items():
            if k == 'user':
                setattr(instance, k, user)
            else:
                setattr(instance, k, v)
        instance.save()
        return instance