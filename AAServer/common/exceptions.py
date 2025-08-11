#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : exceptions.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/11 14:22 
@Version : 1.0
"""
class AuthenticationFailed(Exception):
    """
    身份验证失败异常
    """
    def __init__(self, message="身份验证失败"):
        super().__init__(message)
        self.message = message