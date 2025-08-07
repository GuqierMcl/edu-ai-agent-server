#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : serializers.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/6 16:17 
@Version : 1.0
"""
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.auth.models import LoginParam


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = LoginParam
        fields = "__all__"

    def validate(self, attrs):
        account = attrs.get('account')
        password = attrs.get('password')
        
        if not account:
            raise ValidationError({'account': '账号不能为空'})
        if not password:
            raise ValidationError({'password': '密码不能为空'})
        
