#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : urls.py.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/11 15:19 
@Version : 1.0
"""
from django.urls import path, include

import apps.auth.views

urlpatterns = [
    path('/login', apps.auth.views.login),
    path('/logout', apps.auth.views.logout),
    path('/refresh', apps.auth.views.refresh_token),
]