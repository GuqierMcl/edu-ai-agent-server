#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
应用全局常量
@Project : AAServer 
@File    : constants.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/13 13:03 
@Version : 1.0
"""
class Code:
    CODE_TYPE = [
        {
            'name': '教师职业',
            'type': 'teacher_profession'
        },
        {
            'name': '学生身份',
            'type': 'student_identity'
        },
        {
            'name': '教师职称',
            'type': 'teacher_title'
        }
    ]

class Resource:
    """
    资源相关常量
    type < 0 为系统内置资源，用户不可修改
    """
    RESOURCE_TYPE = [
        {
            'name': '用户头像（系统）',
            'type': -1
        },
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

class User:
    """
    用户相关常量
    """
    USER_TYPE_ADMIN   = 0  # 管理员
    USER_TYPE_TEACHER = 1  # 教师
    USER_TYPE_STUDENT = 2  # 学生