from django.db import models

from AAServer.common.models import BaseModel
from apps.auth.models import User


class Student(BaseModel):
    """
    学生模型
    """
    id = models.BigIntegerField(primary_key=True, db_comment='学生ID')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, db_comment='用户ID', blank=True, null=True)
    identity = models.IntegerField(blank=True, null=True,
                                   db_comment='学生身份, 0表示小学，1表示初中，2表示高中，3表示大学， 4表示硕士研究生，5表示博士研究生, 6表示其他')

    # ---------- 学籍信息 ----------
    student_no = models.CharField(blank=True, null=True, max_length=32, db_comment='学号')
    school_no = models.CharField(max_length=32, blank=True, null=True, db_comment='学校编号')
    enrollment = models.DateField(blank=True, null=True, db_comment='入学日期')

    # ---------- 个人档案 ----------
    birth_date = models.DateField(blank=True, null=True, db_comment='出生日期')
    gender = models.IntegerField(
        choices=[(1, '男'), (0, '女')],
        blank=True, null=True, db_comment='性别'
    )
    address = models.CharField(max_length=255, blank=True, null=True, db_comment='现住址')

    # ---------- 系统运营 ----------
    status = models.IntegerField(
        blank=True, null=True,
        choices=[(0, '在读'), (1, '休学'), (2, '毕业'), (3, '退学')],
        default=0, db_comment='学生状态'
    )

    remark = models.TextField(blank=True, null=True, db_comment='备注')

    class Meta:
        db_table = 'tb_student'
        db_table_comment = "学生信息表"
        ordering = ['-create_time']

    def __str__(self):
        return self.id
