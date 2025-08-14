#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : AAServer 
@File    : pagination.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/12 17:21 
@Version : 1.0
"""
from rest_framework.pagination import PageNumberPagination

from AAServer.response import R


class CwsPageNumberPagination(PageNumberPagination):
    # 覆盖默认的PAGE_SIZE = None
    page_size = 10
    # 自定义页面大小参数
    page_size_query_param = 'pageSize'
    # 设置每页最大数据量, 默认为None，就是不限制
    max_page_size = 100
    # 自定义页码参数
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return R.success({
            'records': data,
            'totalPage': self.page.paginator.num_pages,
            'total': self.page.paginator.count,
            'size': self.page_size,
            'current': self.page.number,
        })
