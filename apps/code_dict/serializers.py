#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : serializers.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/13 11:37 
@Version : 1.0
"""

from rest_framework import serializers
from apps.code_dict.models import Code

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'
        read_only_fields = ('id', 'create_time', 'create_user', 'update_time', 'update_user', 'is_del')
        extra_kwargs = {
            'code': {'required': True, 'max_length': 255},
            'type': {'required': True, 'max_length': 255},
            'name': {'required': True, 'max_length': 255},
            'sequence': {'required': False}
        }