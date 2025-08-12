#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : serializers.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/12 15:04 
@Version : 1.0
"""
from rest_framework.serializers import ModelSerializer
from .models import Resource


class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ResourceSerializer, self).__init__(*args, **kwargs)
        self.fields['id'].required = False
        self.fields['size'].required = False
        self.fields['group_name'].required = False
        self.fields['remote_file_url'].required = False
        self.fields['old_filename'].required = False
        self.fields['sequence'].required = False
