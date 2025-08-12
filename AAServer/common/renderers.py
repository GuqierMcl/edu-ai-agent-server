#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : renderers.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/12 20:11 
@Version : 1.0
"""
import json
from rest_framework.renderers import JSONRenderer

class NumToStrJSONRenderer(JSONRenderer):
    """
    把响应里所有 int/float/Decimal 递归转成字符串
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        def _convert(obj):
            if isinstance(obj, dict):
                return {k: _convert(v) for k, v in obj.items()}
            if isinstance(obj, list):
                return [_convert(item) for item in obj]
            if isinstance(obj, (int, float)):
                return str(obj)
            return obj

        data = _convert(data)
        return super().render(data, accepted_media_type, renderer_context)