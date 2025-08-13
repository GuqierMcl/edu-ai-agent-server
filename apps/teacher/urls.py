#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : urls.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/13 15:47 
@Version : 1.0
"""
from django.urls import path

import apps.teacher.views

urlpatterns = [
    path('/mng', apps.teacher.views.TeacherMngView.as_view(), name='teacher_mng'),
]