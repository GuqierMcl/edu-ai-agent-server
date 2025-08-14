from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from redis.commands.search.reducers import count
from rest_framework.views import APIView

from AAServer.common.pagination import CwsPageNumberPagination
from AAServer.response import R, ResponseEnum
from apps.auth.models import User
from apps.student.models import Student
from apps.student.serializers import StudentCreateSerializer, StudentSerializer, StudentFlatUpdateSerializer

FILTERS = {
    'name': 'user__name__icontains',
    'account': 'user__account__icontains',
    'phone': 'user__phone__icontains',
    'email': 'user__email__icontains',
    'identity': 'identity',
    'student_no': 'student_no__icontains',
    'school_no': 'school_no__icontains',
    'gender': 'gender',
    'status': 'status',
    'remark': 'remark__icontains',
}

class StudentMngView(APIView):
    """
    学生管理视图
    """

    @transaction.atomic
    def post(self, request):
        """
        创建学生
        """
        serializer = StudentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return R.success({
            'student_id': student.id,
            'user_id': student.user.id,
        })

    def get(self, request):
        """
        分页获取学生信息
        :param request:
        :return:
        """
        # 1. 收集非空参数
        params = {k: request.GET.get(k, '').strip() or None for k in FILTERS}
        params = {k: v for k, v in params.items() if v is not None}

        # 2. 动态构造 Q 查询
        q_objects = Q()
        for k, v in params.items():
            q_objects &= Q(**{FILTERS[k]: v})

        qs = Student.objects.filter(q_objects).order_by('-create_time')

        # 3. 分页
        paginator = CwsPageNumberPagination()
        page = paginator.paginate_queryset(qs, request)
        serializer = StudentSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def delete(self, request):
        """
        删除学生信息（逻辑删除）
        """
        ids = request.GET.getlist('ids')
        if not ids:
            return R.fail(ResponseEnum.PARAM_IS_BLANK)
        qs = Student.objects.filter(id__in=ids)
        count = qs.count()
        if count == 0:
            return R.fail(ResponseEnum.PARAM_IS_BLANK)

        user_ids = qs.values_list('user_id', flat=True).distinct()

        deleted_count = qs.delete()  # 逻辑删除

        User.objects.filter(id__in=user_ids).delete()

        return R.success({
            'deleted_count': deleted_count
        })

    @transaction.atomic
    def put(self, request):
        """
        更新学生信息
        """
        student = Student.objects.get(id=request.data.get('id'))
        serializer = StudentFlatUpdateSerializer(
            instance=student,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return R.success()