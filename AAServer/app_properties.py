#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
应用全局常量
@Project : AAServer 
@File    : app_properties.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/13 13:03 
@Version : 1.0
"""
class Code:
    CODE_TYPE = [
        {
            'name': '智能体类型',
            'type': 'ai_type'
        },
        {
            'name': '智能体状态',
            'type': 'ai_status'
        },
        {
            'name': '智能体能力',
            'type': 'ai_ability'
        },
        {
            'name': '智能体模型',
            'type': 'ai_model'
        },
        {
            'name': '智能体语言',
            'type': 'ai_language'
        },
        {
            'name': '智能体领域',
            'type': 'ai_domain'
        },
    ]

class Resource:
    """
    资源相关常量
    """
    RESOURCE_TYPE = [
        {
            'name': '图片资源',
            'type': 0
        },
        {
            'name': '文档资源',
            'type': 1
        },
        {
            'name': '视频资源',
            'type': 2
        },
        {
            'name': '音频资源',
            'type': 3
        },
        {
            'name': '代码资源',
            'type': 4
        },
        {
            'name': '其他资源',
            'type': 5
        }
    ]

    RESOURCE_STATUS = [
        {
            'name': '可用',
            'status': 1
        },
        {
            'name': '不可用',
            'status': 0
        }
    ]