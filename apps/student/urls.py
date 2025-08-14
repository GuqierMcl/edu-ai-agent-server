#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : urls.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/14 11:56 
@Version : 1.0
"""
from django.urls import path

import apps.student.views

urlpatterns = [
    path('/mng', apps.student.views.StudentMngView.as_view()),
]