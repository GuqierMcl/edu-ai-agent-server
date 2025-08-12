#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : urls.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/12 15:20 
@Version : 1.0
"""
from django.urls import path

import apps.resource.views
urlpatterns = [
    # 这里可以添加资源相关的URL路由
    path('/upload', apps.resource.views.upload_resource),
]