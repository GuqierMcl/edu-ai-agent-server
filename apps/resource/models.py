from django.db import models

from AAServer.common.models import BaseModel


# Create your models here.
class Resource(BaseModel):
    id = models.BigIntegerField(primary_key=True, db_comment='资源ID')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='资源名称')
    type = models.IntegerField(blank=True, null=True, db_comment='资源类型，0为图片，1为pdf...')
    group_name = models.CharField(max_length=255, blank=True, null=True, db_comment='文件组名')
    remote_file_url = models.CharField(max_length=255, blank=True, null=True, db_comment='远程文件路径')
    old_filename = models.CharField(max_length=255, blank=True, null=True, db_comment='源文件名')
    sequence = models.IntegerField(blank=True, null=True, db_comment='同层级排序')


    class Meta:
        db_table = 'sys_resource'
        db_table_comment = '文件资源表'