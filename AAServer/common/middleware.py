#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
通用中间件
@Project : AAServer 
@File    : middleware.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/7 13:29 
@Version : 1.0
"""
import threading
from django.utils.deprecation import MiddlewareMixin

_thread_locals = threading.local()

class CurrentUserMiddleware(MiddlewareMixin):
    """把当前登录用户塞进线程局部变量"""
    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)

    def process_response(self, request, response):
        _thread_locals.user = None
        return response
