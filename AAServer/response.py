#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
通用响应封装
@Project : AAServer
@File    : response.py
@IDE     : PyCharm
@Author  : Guqier
@Date    : 2025/8/6 13:59
@Version : 1.0
"""
from rest_framework.response import Response


class CodeMsg:
    code = 1
    msg = 'success'

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return f'code: {self.code}, msg: {self.msg}'


class ResponseEnum:
    """
    通用状态码
    """
    SUCCESS = CodeMsg(1, "success")
    ERROR = CodeMsg(0, "error")

    """
    业务错误状态码
    """
    PARAM_IS_INVAlID = CodeMsg(101, "参数无效"),

    PARAM_IS_BLANK = CodeMsg(102, "必要参数为空"),

    NOTE_NOT_EXIST = CodeMsg(103, "笔记不存在"),

    """
    用户错误
    201 - 299
    """
    USER_NOT_LOGIN = CodeMsg(201, "用户未登录"),
    INVALID_TOKEN = CodeMsg(202, "无效Token信息"),
    USER_NOT_EXIST = CodeMsg(203, "用户不存在"),
    USER_LOGIN_ERROR = CodeMsg(204, "登陆失败，账号或者密码有误"),
    NOT_PERMISSION = CodeMsg(205, "无权限访问"),
    TOKEN_EXPIRED = CodeMsg(206, "Token已过期"),
    NOT_FOR_STUDENT = CodeMsg(207, "管理后台仅限教师或管理员登录"),
    ERROR_AUTH_CODE = CodeMsg(208, "验证码错误"),
    WX_ERROR = CodeMsg(209, "微信验证错误"),
    CODE_EMPTY = CodeMsg(210, "CODE不存在"),
    WX_USER_NEED_BIND = CodeMsg(211, "未绑定账号"),
    WX_USER_BIND_ERROR = CodeMsg(212, "绑定账号失败"),

    """
    业务错误
    301 - 399 
    """
    DATA_NOT_FOUND = CodeMsg(301, "没有数据"),
    HANDLE_FAIL = CodeMsg(302, "业务处理失败"),

    DATABASE_OPERATION_FAIL = CodeMsg(303, "数据库操作失败"),
    UPLOAD_FAIL = CodeMsg(304, "文件上传失败"),
    DAILY_ALREADY_FINISHED = CodeMsg(305, "每日一练已完成"),
    GROUP_JOIN_COUNT_MAX = CodeMsg(306, "加入小组数已最大"),
    GROUP_INVITATION_CODE_INVALID = CodeMsg(307, "邀请码不存在或已过期"),
    TEST_PAPER_INVALID = CodeMsg(308, "试卷不存在或已删除"),
    SYSTEM_ERROR = CodeMsg(999, "系统异常"),

    """
    数据错误
    """
    CACHE_NOT_EXIST = CodeMsg(401, "缓存不存在或已过期");


class R:

    @staticmethod
    def success(code_msg=ResponseEnum.SUCCESS, data=None):
        return Response({'code': code_msg.code, 'msg': code_msg.msg, 'data': data})

    @staticmethod
    def fail(code_msg, data=None):
        return Response({'code': code_msg.code, 'msg': code_msg.msg, 'data': data})

    @staticmethod
    def fail_code_msg(code, msg, data=None):
        return Response({'code': code, 'msg': msg, 'data': data})
