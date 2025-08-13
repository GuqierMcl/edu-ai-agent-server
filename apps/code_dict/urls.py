#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : urls.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/13 11:35 
@Version : 1.0
"""
from django.urls import path

import apps.code_dict.views
from apps.code_dict.views import CodeView

urlpatterns = [
    path('', CodeView.as_view()),
    path('/options/<str:type_name>', apps.code_dict.views.get_options),
    path('/type', apps.code_dict.views.get_code_type),
]