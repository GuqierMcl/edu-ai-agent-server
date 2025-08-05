# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class SysUser(AbstractBaseUser):
    id = models.BigIntegerField(primary_key=True, db_comment='用户ID')
    account = models.CharField(max_length=255, blank=True, null=True, db_comment='账号')
    password = models.CharField(max_length=255, blank=True, null=True, db_comment='密码')
    salt = models.CharField(max_length=255, blank=True, null=True, db_comment='盐值')
    nickname = models.CharField(max_length=255, blank=True, null=True, db_comment='昵称')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='真实姓名')
    phone = models.CharField(max_length=255, blank=True, null=True, db_comment='手机号')
    email = models.CharField(max_length=255, blank=True, null=True, db_comment='电子邮箱')
    type = models.IntegerField(blank=True, null=True, db_comment='用户类型，0表示管理员，1表示教师，2表示学生')
    avatar = models.BigIntegerField(blank=True, null=True, db_comment='头像ID，值为tb_image图片ID')
    expired_time = models.DateTimeField(blank=True, null=True, db_comment='有效期')
    del_field = models.IntegerField(db_column='del', blank=True, null=True, db_comment='逻辑删除')  # Field renamed because it was a Python reserved word.
    create_time = models.DateTimeField(blank=True, null=True, db_comment='创建时间')

    class Meta:
        managed = False
        db_table = 'sys_user'
        db_table_comment = '用户表'
