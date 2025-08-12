#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
通用模型管理类
@Project : AAServer 
@File    : manager.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/7 12:27 
@Version : 1.0
"""
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models import QuerySet


class LogicalDeleteQuerySet(QuerySet):
    """
    逻辑删除支持QuerySet
    """

    def delete(self):
        return super(LogicalDeleteQuerySet, self).update(is_del=1)


class ModelManager(models.Manager):
    """
    支持逻辑删除的模型管理器
    """

    def get_queryset(self):
        return LogicalDeleteQuerySet(self.model).filter(is_del=0)
