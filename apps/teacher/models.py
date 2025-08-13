from django.db import models

from AAServer.common.models import BaseModel
from apps.auth.models import User
from apps.code_dict.models import Code

class Teacher(BaseModel):
    """
    教师模型
    """
    id = models.BigIntegerField(primary_key=True, db_comment='教师ID')
    user = models.ForeignKey(User, db_comment='用户ID', on_delete=models.RESTRICT)
    stu_friendly_name = models.CharField(max_length=100, null=True, blank=True, db_comment="师生称呼")
    profession = models.IntegerField(null=True, blank=True, db_comment="职业, 如教师、教授等")
    department = models.CharField(max_length=100, null=True, blank=True, db_comment="部门")

    class Meta:
        db_table = 'tb_teacher'
        db_table_comment = "教师信息表"

    def __str__(self):
        return self.stu_friendly_name
