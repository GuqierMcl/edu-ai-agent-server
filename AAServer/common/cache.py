#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : cache.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/13 16:21 
@Version : 1.0
"""
from django.core.cache import cache

CACHE_PREFIX = 'API:'

def cache_get(key, default=None):
    return cache.get(CACHE_PREFIX + key, default)

def cache_set(key, value, ttl=300):
    cache.set(CACHE_PREFIX + key, value, ttl)

def cache_del(key):
    cache.delete(CACHE_PREFIX + key)