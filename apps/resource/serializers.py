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
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from AAServer import constants
from .models import Resource
import django.conf

ENDPOINT = django.conf.settings.MINIO_ENDPOINT
USE_HTTPS = django.conf.settings.MINIO_USE_HTTPS
BUCKETS = django.conf.settings.MINIO_PUBLIC_BUCKETS


class ResourceSerializer(ModelSerializer):
    remote_file_url = serializers.SerializerMethodField(read_only=True)  # 远程文件URL
    type_name = serializers.SerializerMethodField(read_only=True)

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

    def get_remote_file_url(self, obj):
        return f'{"https" if USE_HTTPS else "http"}://{ENDPOINT}/{BUCKETS[0]}/{obj.file}'

    def get_type_name(self, obj):
        type_dict = {item['type']: item['name'] for item in constants.Resource.RESOURCE_TYPE}
        return type_dict.get(obj.type, '未知')


class ResourceUpdateSerializer(ResourceSerializer):

    class Meta:
        model = Resource
        exclude = ['file']

    def __init__(self, *args, **kwargs):
        super(ResourceUpdateSerializer, self).__init__(*args, **kwargs)