# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

from AAServer.common.middleware import get_current_user_id
from AAServer.common.models import BaseModel
from AAServer.common.snowflake import next_id


class User(AbstractBaseUser, BaseModel):
    USERNAME_FIELD = 'account'

    id = models.BigIntegerField(primary_key=True, db_comment='用户ID')
    account = models.CharField(max_length=255, blank=True, null=True, db_comment='账号', unique=True)
    password = models.CharField(max_length=255, blank=True, null=True, db_comment='密码')
    nickname = models.CharField(max_length=255, blank=True, null=True, db_comment='昵称')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='真实姓名')
    phone = models.CharField(max_length=255, blank=True, null=True, db_comment='手机号')
    email = models.CharField(max_length=255, blank=True, null=True, db_comment='电子邮箱')
    type = models.IntegerField(blank=True, null=True, db_comment='用户类型，0表示管理员，1表示教师，2表示学生')
    avatar = models.BigIntegerField(blank=True, null=True, db_comment='头像ID，值为tb_image图片ID')
    expired_time = models.DateTimeField(blank=True, null=True, db_comment='账号到期时间')
    last_login = models.DateTimeField(blank=True, null=True, db_comment='上一次登录时间')
    is_del = models.IntegerField(db_column='del', blank=True, null=True,
                                    db_comment='逻辑删除')
    create_time = models.DateTimeField(blank=True, null=True, db_comment='创建时间')

    class Meta:
        managed = True
        db_table = 'sys_user'
        db_table_comment = '用户表'

    def __str__(self):
        return self.account

class LoginParam(models.Model):
    account = models.CharField()
    password = models.CharField()

    class Meta:
        abstract = True

class Code(BaseModel):
    id = models.BigIntegerField(primary_key=True, db_comment='码表ID')
    code = models.CharField(max_length=255, blank=True, null=True, db_comment='码')
    type = models.CharField(max_length=255, blank=True, null=True, db_comment='类型')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='名称')
    sequence = models.IntegerField(blank=True, null=True, db_comment='排序')


    class Meta:
        managed = False
        db_table = 'sys_code'
        db_table_comment = '码表（数据字典）'