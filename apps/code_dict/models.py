from django.db import models

from AAServer.common.models import BaseModel


# Create your models here.

class Code(BaseModel):
    id = models.BigIntegerField(primary_key=True, db_comment='码表ID')
    code = models.CharField(max_length=255, blank=True, null=True, db_comment='码')
    type = models.CharField(max_length=255, blank=True, null=True, db_comment='类型')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='名称')
    sequence = models.IntegerField(blank=True, null=True, db_comment='排序')


    class Meta:
        db_table = 'sys_code'
        db_table_comment = '码表（数据字典）'