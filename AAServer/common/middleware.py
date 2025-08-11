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

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

_thread_locals = threading.local()

class CurrentUserMiddleware(MiddlewareMixin):
    """把当前登录用户塞进线程局部变量"""
    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)

    def process_response(self, request, response):
        _thread_locals.user = None
        return response

class CorsMiddleware:
    """处理跨域请求的中间件"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'OPTIONS':
            response = HttpResponse(status=200)
        else:
            response = self.get_response(request)

        response['Access-Control-Allow-Origin']  = request.headers.get('Origin', '*')
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'content-type, Authorization'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response